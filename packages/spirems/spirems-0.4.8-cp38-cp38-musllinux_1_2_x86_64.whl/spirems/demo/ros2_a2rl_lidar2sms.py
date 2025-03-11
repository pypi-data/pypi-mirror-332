#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, Image
import time
import os
import numpy as np
import ros2_numpy
import cv2
from spirems import Publisher, Subscriber, def_msg, cvimg2sms


"""
依赖项安装：
pip install spirems ros2-numpy
"""

DEFAULT_IP = "127.0.0.1"


class A2RLLidar2SMSNode(Node):
    def __init__(self):
        Node.__init__(self, 'A2RLLidar2SMSNode')

        self.sensor_lidar_front_sub = self.create_subscription(
            PointCloud2,
            "/flyeagle/lidar_front/points",
            self.sensor_lidar_front_callback,
            10
        )
        self.sensor_lidar_left_sub = self.create_subscription(
            PointCloud2,
            "/flyeagle/lidar_left/points",
            self.sensor_lidar_left_callback,
            10
        )
        self.sensor_lidar_right_sub = self.create_subscription(
            PointCloud2,
            "/flyeagle/lidar_right/points",
            self.sensor_lidar_right_callback,
            10
        )

        self.sms_lidar_front_pub = Publisher("/flyeagle/lidar_front", "memory_msgs::RawImage", ip=DEFAULT_IP)
        self.sms_lidar_left_pub = Publisher("/flyeagle/lidar_left", "memory_msgs::RawImage", ip=DEFAULT_IP)
        self.sms_lidar_right_pub = Publisher("/flyeagle/lidar_right", "memory_msgs::RawImage", ip=DEFAULT_IP)
    
    def sensor_lidar_front_callback(self, msg):
        t1 = time.time()
        cloud_arr = np.frombuffer(msg.data, np.float32).reshape(-1, 6)
        pcd_ = cloud_arr[:, [1,2,3]].copy(order='C')  # ros2_numpy.numpify(msg)['xyz']
        sms_msg = self.sms_lidar_front_pub.cvimg2sms_mem(pcd_)
        ros_time = msg.header.stamp
        total_seconds = ros_time.sec + ros_time.nanosec / 1e9
        sms_msg['timestamp'] = total_seconds
        sms_msg['t1'] = time.time()
        print("total_seconds:", total_seconds)
        self.sms_lidar_front_pub.publish(sms_msg)
        print("dt:", time.time() - t1)
    
    def sensor_lidar_left_callback(self, msg):
        cloud_arr = np.frombuffer(msg.data, np.float32).reshape(-1, 6)
        pcd_ = cloud_arr[:, [1,2,3]].copy(order='C')  # ros2_numpy.numpify(msg)['xyz']
        sms_msg = self.sms_lidar_left_pub.cvimg2sms_mem(pcd_)
        ros_time = msg.header.stamp
        total_seconds = ros_time.sec + ros_time.nanosec / 1e9
        sms_msg['timestamp'] = total_seconds
        self.sms_lidar_left_pub.publish(sms_msg)
    
    def sensor_lidar_right_callback(self, msg):
        cloud_arr = np.frombuffer(msg.data, np.float32).reshape(-1, 6)
        pcd_ = cloud_arr[:, [1,2,3]].copy(order='C')  # ros2_numpy.numpify(msg)['xyz']
        sms_msg = self.sms_lidar_right_pub.cvimg2sms_mem(pcd_)
        ros_time = msg.header.stamp
        total_seconds = ros_time.sec + ros_time.nanosec / 1e9
        sms_msg['timestamp'] = total_seconds
        self.sms_lidar_right_pub.publish(sms_msg)


def main(args=None):
    rclpy.init(args=args)
    node = A2RLLidar2SMSNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()