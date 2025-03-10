#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author: renjin@bit.edu.cn
# @Date  : 2024-07-08

import socket
import threading
import time
import random
from spirems.log import get_logger
from spirems.error_code import ec2str
from spirems.msg_helper import (get_all_msg_types, def_msg, encode_msg, check_topic_url, decode_msg, check_msg,
                                index_msg_header, decode_msg_header, QoS)


logger = get_logger('Subscriber')


class Subscriber(threading.Thread):
    def __init__(
        self,
        topic_url: str,
        topic_type: str,
        callback_func: callable,
        ip: str = '127.0.0.1',
        port: int = 9094,
        qos: QoS = QoS.BestEffort
    ):
        threading.Thread.__init__(self)
        self.topic_url = topic_url
        self.topic_type = topic_type
        self.ip = ip
        self.port = port
        self.callback_func = callback_func
        self.qos = qos
        self._send_lock = threading.Lock()

        all_types = get_all_msg_types()
        if topic_type not in all_types.keys():
            raise ValueError('({}) {}'.format(topic_type, ec2str(205)))
        url_state = check_topic_url(topic_url)
        if url_state != 0:
            raise ValueError('({}) {}'.format(topic_url, ec2str(url_state)))

        self.last_send_time = 0.0
        self.force_quit = False
        self.heartbeat_thread = None
        self.heartbeat_running = False
        self.running = True
        try:
            self._link()
        except Exception as e:
            logger.warning("({}) __init__: {}".format(self.topic_url, e))
        self.start()

    def kill(self):
        self.force_quit = True

    def wait_key(self):
        try:
            while not self.force_quit:
                time.sleep(0.5)
        except KeyboardInterrupt:
            logger.info('stopped by keyboard')
            self.kill()
            self.join()

    def heartbeat(self):
        while self.heartbeat_running:
            try:
                if time.time() - self.last_send_time >= 2.0:
                    apply_topic = def_msg('_sys_msgs::Subscriber')
                    apply_topic['topic_type'] = self.topic_type
                    apply_topic['url'] = self.topic_url
                    apply_topic['qos'] = self.qos.value
                    with self._send_lock:
                        self.client_socket.sendall(encode_msg(apply_topic))
                    self.last_send_time = time.time()
            except Exception as e:
                logger.warning("({}) heartbeat: {}".format(self.topic_url, e))

            time.sleep(random.randint(1, 3))
            if self.force_quit:
                self.heartbeat_running = False
                break

    def _link(self):
        self.heartbeat_running = False
        if self.heartbeat_thread is not None:
            self.heartbeat_thread.join()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024 * 128)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024 * 8)
        self.client_socket.settimeout(5)
        self.client_socket.connect((self.ip, self.port))
        self.heartbeat_thread = threading.Thread(target=self.heartbeat)
        self.heartbeat_running = True
        self.heartbeat_thread.start()

    def suspend(self):
        if self.running and self.heartbeat_running:
            try:
                suspend_msg = def_msg('_sys_msgs::Suspend')
                with self._send_lock:
                    self.client_socket.sendall(encode_msg(suspend_msg))
                self.last_send_time = time.time()
            except Exception as e:
                logger.warning("({}) suspend: {}".format(self.topic_url, e))

    def unsuspend(self):
        if self.running and self.heartbeat_running:
            try:
                suspend_msg = def_msg('_sys_msgs::Unsuspend')
                with self._send_lock:
                    self.client_socket.sendall(encode_msg(suspend_msg))
                self.last_send_time = time.time()
            except Exception as e:
                logger.warning("({}) unsuspend: {}".format(self.topic_url, e))

    def _parse_msg(self, msg):
        success, decode_data = decode_msg(msg)
        if success and decode_data['type'] == '_sys_msgs::TopicDown':
            # print("{:.3f}: {}".format(time.time() - decode_data['timestamp'], decode_data))
            self.callback_func(decode_data['topic'])
            response = def_msg('_sys_msgs::Result')
            response['id'] = decode_data['id']
            with self._send_lock:
                self.client_socket.sendall(encode_msg(response))
            self.last_send_time = time.time()
        elif success and decode_data['type'] == '_sys_msgs::Result':
            if decode_data['error_code'] > 0:
                logger.error(ec2str(decode_data['error_code']))
        elif not success:
            logger.debug(msg)

    def run(self):
        data = b''
        last_data = b''
        big_msg = 0
        while self.running:
            if self.force_quit:
                self.running = False
                break
            try:
                data = self.client_socket.recv(1024 * 1024)  # 1M
                if not data:
                    raise TimeoutError('No data arrived.')
                # print('data: {}'.format(data))
            except TimeoutError as e:
                logger.warning("({}) recv(1): {}".format(self.topic_url, e))
                # print(time.time() - tt1)
                self.running = False
                data = b''
            except Exception as e:
                logger.warning("({}) recv(2): {}".format(self.topic_url, e))
                self.running = False
                data = b''

            try:
                recv_msgs = []
                checked_msgs, parted_msgs, parted_lens = check_msg(data)

                if len(parted_msgs) > 0:
                    for parted_msg, parted_len in zip(parted_msgs, parted_lens):
                        if parted_len > 0:
                            last_data = parted_msg
                            big_msg = parted_len
                        else:
                            last_data += parted_msg
                            if 0 < big_msg <= len(last_data):
                                recv_msgs.append(last_data[:big_msg])
                                big_msg = 0
                                last_data = b''

                recv_msgs.extend(checked_msgs)
                if len(recv_msgs) > 0:
                    for msg in recv_msgs:
                        self._parse_msg(msg)

            except Exception as e:
                logger.warning("({}) parse: {}".format(self.topic_url, e))
                self.running = False

            while not self.running:
                if self.force_quit:
                    break
                # logger.info('(1) running=False, heartbeat_running=False')
                self.heartbeat_running = False
                try:
                    self.client_socket.close()
                    # logger.info('(2) client_socket closed')
                except Exception as e:
                    logger.warning("({}) socket_close: {}".format(self.topic_url, e))
                time.sleep(5)
                # logger.info('(3) start re-linking ...')
                try:
                    self._link()
                    self.running = True
                    # logger.info('(4) running=True, suspended=False')
                except Exception as e:
                    logger.warning("({}) relink: {}".format(self.topic_url, e))
                logger.info('Running={}, Wait ...'.format(self.running))
                data = b''
                last_data = b''
                big_msg = 0


max_dt = 0


def callback_f(msg):
    global max_dt
    print("Dt: {}, Data: {}".format(time.time() - msg['timestamp'], msg['data']))
    if time.time() - msg['timestamp'] > max_dt:
        max_dt = time.time() - msg['timestamp']
        print("Max-Dt: {}".format(max_dt))


if __name__ == '__main__':
    sub = Subscriber('/sensors/hello/a12', 'std_msgs::NumberMultiArray', callback_f,
                     ip='127.0.0.1')
    # sub.wait_key()

    sus = False
    while True:
        if not sus:
            print("sub.suspend()")
            sub.suspend()
            sus = True
        else:
            print("sub.unsuspend()")
            sub.unsuspend()
            sus = False
        time.sleep(10)
