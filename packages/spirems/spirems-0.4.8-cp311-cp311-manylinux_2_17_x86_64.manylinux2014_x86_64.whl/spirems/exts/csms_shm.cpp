#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <random>  // 用于生成随机数
#include <iostream>
#include <string>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#pragma comment(lib, "rt")


namespace py = pybind11;


class RunStat
{
public:
    RunStat() {}
    ~RunStat() {}
private:
    static RunStat* p;
public:
    static RunStat* instance()
    {
        return p;
    }
    py::dict shm_pubs;
    py::dict shm_subs;
    std::vector<char*> shm_ptrs;
};


RunStat* RunStat::p = new RunStat;
const int g_shm_size = 1024 * 1024 * 120;


void init_submem(const std::string mem_name)
{
    int shm_fd = shm_open(mem_name.c_str(), O_RDONLY, 0666);
    if (shm_fd == -1)
    {
        throw std::runtime_error("Failed to create shared memory object");
        // std::cerr << "Failed to create shared memory object" << std::endl;
        // std::abort();
    }
    char* shm_ptr = (char*)mmap(0, g_shm_size, PROT_READ, MAP_SHARED, shm_fd, 0);
    if (shm_ptr == MAP_FAILED)
    {
        throw std::runtime_error("Failed to map shared memory");
        // std::cerr << "Failed to map shared memory" << std::endl;
        // std::abort();
    }

    int ptr_id = static_cast<int>(RunStat::instance()->shm_ptrs.size());
    RunStat::instance()->shm_ptrs.push_back(shm_ptr);
    RunStat::instance()->shm_subs[mem_name.c_str()] = py::dict();
    RunStat::instance()->shm_subs[mem_name.c_str()]["fd"] = shm_fd;
    RunStat::instance()->shm_subs[mem_name.c_str()]["ptr_id"] = ptr_id;
    // std::cout << "init_submem" << std::endl;
}


void init_pubmem(const std::string mem_name)
{
    int shm_fd = shm_open(mem_name.c_str(), O_CREAT | O_RDWR, 0666);
    if (shm_fd == -1)
    {
        throw std::runtime_error("Failed to create shared memory object");
        // std::cerr << "Failed to create shared memory object" << std::endl;
        // std::abort();
    }
    if (ftruncate(shm_fd, g_shm_size) == -1)
    {
        throw std::runtime_error("Failed to set shared memory size");
        // std::cerr << "Failed to set shared memory size" << std::endl;
        // std::abort();
    }
    char* shm_ptr = (char*)mmap(0, g_shm_size, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    if (shm_ptr == MAP_FAILED)
    {
        throw std::runtime_error("Failed to map shared memory");
        // std::cerr << "Failed to map shared memory" << std::endl;
        // std::abort();
    }

    int ptr_id = static_cast<int>(RunStat::instance()->shm_ptrs.size());
    RunStat::instance()->shm_ptrs.push_back(shm_ptr);
    RunStat::instance()->shm_pubs[mem_name.c_str()] = py::dict();
    RunStat::instance()->shm_pubs[mem_name.c_str()]["offset"] = 0;
    RunStat::instance()->shm_pubs[mem_name.c_str()]["fd"] = shm_fd;
    RunStat::instance()->shm_pubs[mem_name.c_str()]["ptr_id"] = ptr_id;
    RunStat::instance()->shm_pubs[mem_name.c_str()]["fst"] = 1;
    // std::cout << RunStat::instance()->shm_pubs.dump() << std::endl;
}


py::array_t<uint8_t> sms2cvimg_uint8(py::dict dict)
{
    std::string type = dict["type"].cast<std::string>();
    std::string encoding = dict["encoding"].cast<std::string>();
    std::string shm_name = dict["shm_name"].cast<std::string>();
    int h = dict["height"].cast<int>();
    int w = dict["width"].cast<int>();
    int offset = dict["offset"].cast<int>();
    int shm_fst = dict["shm_fst"].cast<int>();

    if (!RunStat::instance()->shm_subs.contains(shm_name.c_str()) || 1 == shm_fst)
    {
        init_submem(shm_name);
    }

    int ptr_id = RunStat::instance()->shm_subs[shm_name.c_str()]["ptr_id"].cast<int>();
    char* shm_ptr = RunStat::instance()->shm_ptrs[ptr_id];
    shm_ptr = shm_ptr + offset;

    int tp = 0;
    if ("8UC1" == encoding)
        tp = 1;
    else if ("8UC2" == encoding)
        tp = 2;
    else if ("8UC3" == encoding)
        tp = 3;
    else if ("8UC4" == encoding)
        tp = 4;
    else
    {
        throw std::runtime_error("Unsupported sms::encoding type!");
    }

    py::array_t<uint8_t> result({h, w, tp});
    py::buffer_info buf = result.request();
    std::memcpy(buf.ptr, shm_ptr, h * w * tp);
    
    if (RunStat::instance()->shm_ptrs[ptr_id] == MAP_FAILED)
    {
        throw std::runtime_error("Failed to map shared memory!");
    }

    return result;
}


py::array_t<uint16_t> sms2cvimg_uint16(py::dict dict)
{
    std::string type = dict["type"].cast<std::string>();
    std::string encoding = dict["encoding"].cast<std::string>();
    std::string shm_name = dict["shm_name"].cast<std::string>();
    int h = dict["height"].cast<int>();
    int w = dict["width"].cast<int>();
    int offset = dict["offset"].cast<int>();
    int shm_fst = dict["shm_fst"].cast<int>();

    if (!RunStat::instance()->shm_subs.contains(shm_name.c_str()) || 1 == shm_fst)
    {
        init_submem(shm_name);
    }

    int ptr_id = RunStat::instance()->shm_subs[shm_name.c_str()]["ptr_id"].cast<int>();
    char* shm_ptr = RunStat::instance()->shm_ptrs[ptr_id];
    shm_ptr = shm_ptr + offset;

    int tp = 0;
    if ("16UC1" == encoding)
        tp = 1;
    else if ("16UC2" == encoding)
        tp = 2;
    else if ("16UC3" == encoding)
        tp = 3;
    else if ("16UC4" == encoding)
        tp = 4;
    else
    {
        throw std::runtime_error("Unsupported sms::encoding type!");
    }

    py::array_t<uint16_t> result({h, w, tp});
    py::buffer_info buf = result.request();
    std::memcpy(buf.ptr, shm_ptr, h * w * tp * 2);
    
    if (RunStat::instance()->shm_ptrs[ptr_id] == MAP_FAILED)
    {
        throw std::runtime_error("Failed to map shared memory!");
    }

    return result;
}


py::array_t<float> sms2cvimg_float(py::dict dict)
{
    std::string type = dict["type"].cast<std::string>();
    std::string encoding = dict["encoding"].cast<std::string>();
    std::string shm_name = dict["shm_name"].cast<std::string>();
    int h = dict["height"].cast<int>();
    int w = dict["width"].cast<int>();
    int offset = dict["offset"].cast<int>();
    int shm_fst = dict["shm_fst"].cast<int>();

    if (!RunStat::instance()->shm_subs.contains(shm_name.c_str()) || 1 == shm_fst)
    {
        init_submem(shm_name);
    }

    int ptr_id = RunStat::instance()->shm_subs[shm_name.c_str()]["ptr_id"].cast<int>();
    char* shm_ptr = RunStat::instance()->shm_ptrs[ptr_id];
    shm_ptr = shm_ptr + offset;

    int tp = 0;
    if ("32FC1" == encoding)
        tp = 1;
    else if ("32FC2" == encoding)
        tp = 2;
    else if ("32FC3" == encoding)
        tp = 3;
    else if ("32FC4" == encoding)
        tp = 4;
    else
    {
        throw std::runtime_error("Unsupported sms::encoding type!");
    }

    py::array_t<float> result({h, w, tp});
    py::buffer_info buf = result.request();
    std::memcpy(buf.ptr, shm_ptr, h * w * tp * 4);
    
    if (RunStat::instance()->shm_ptrs[ptr_id] == MAP_FAILED)
    {
        throw std::runtime_error("Failed to map shared memory!");
    }

    return result;
}



py::dict cvimg2sms_uint8(py::array_t<uint8_t> input, const std::string& mem_name)
{
    py::buffer_info buf = input.request();
    size_t ndim = input.ndim();
    const auto shape = input.shape();

    std::string encoding;
    int tp = 1;
    if (ndim == 2 || ndim == 3)
    {
        if (ndim == 2)
        {
            encoding = "8UC1";
            tp = 1;
        }
        else
        {
            if (shape[2] == 1)
            {
                encoding = "8UC1";
                tp = 1;
            }
            else if (shape[2] == 2)
            {
                encoding = "8UC2";
                tp = 2;
            }
            else if (shape[2] == 3)
            {
                encoding = "8UC3";
                tp = 3;
            }
            else if (shape[2] == 4)
            {
                encoding = "8UC4";
                tp = 4;
            }
            else
            {
                throw std::runtime_error("Unsupported sms::encoding type!");
            }
        }
    }
    else
    {
        throw std::runtime_error("Unsupported sms::encoding type!");
    }
    int h = shape[0];
    int w = shape[1];

    if (!RunStat::instance()->shm_pubs.contains(mem_name.c_str()))
    {
        init_pubmem(mem_name);
    }
    int ptr_id = RunStat::instance()->shm_pubs[mem_name.c_str()]["ptr_id"].cast<int>();
    char* shm_ptr = RunStat::instance()->shm_ptrs[ptr_id];
    int shm_offset = RunStat::instance()->shm_pubs[mem_name.c_str()]["offset"].cast<int>();
    int shm_fst = RunStat::instance()->shm_pubs[mem_name.c_str()]["fst"].cast<int>();

    py::dict result;
    result["type"] = "memory_msgs::RawImage";
    result["encoding"] = encoding;
    result["shm_name"] = mem_name;
    result["height"] = h;
    result["width"] = w;
    // result["offset"] = 0;
    // result["shm_fst"] = 0;

    if (1 == shm_fst)
    {
        result["shm_fst"] = 1;
        RunStat::instance()->shm_pubs[mem_name.c_str()]["fst"] = 0;
    }
    else
    {
        result["shm_fst"] = 0;
    }

    int img_siz = h * w * tp;  // cvimg.total() * cvimg.elemSize();
    if (shm_offset + img_siz > g_shm_size)
    {
        shm_offset = 0;
    }
    std::memcpy(shm_ptr + shm_offset, buf.ptr, img_siz);
    result["offset"] = shm_offset;
    RunStat::instance()->shm_pubs[mem_name.c_str()]["offset"] = static_cast<int>(shm_offset + img_siz);

    return result;
}


py::dict cvimg2sms_uint16(py::array_t<uint16_t> input, const std::string& mem_name)
{
    py::buffer_info buf = input.request();
    size_t ndim = input.ndim();
    const auto shape = input.shape();

    std::string encoding;
    int tp = 1;
    if (ndim == 2 || ndim == 3)
    {
        if (ndim == 2)
        {
            encoding = "16UC1";
            tp = 1;
        }
        else
        {
            if (shape[2] == 1)
            {
                encoding = "16UC1";
                tp = 1;
            }
            else if (shape[2] == 2)
            {
                encoding = "16UC2";
                tp = 2;
            }
            else if (shape[2] == 3)
            {
                encoding = "16UC3";
                tp = 3;
            }
            else if (shape[2] == 4)
            {
                encoding = "16UC4";
                tp = 4;
            }
            else
            {
                throw std::runtime_error("Unsupported sms::encoding type!");
            }
        }
    }
    else
    {
        throw std::runtime_error("Unsupported sms::encoding type!");
    }
    int h = shape[0];
    int w = shape[1];

    if (!RunStat::instance()->shm_pubs.contains(mem_name.c_str()))
    {
        init_pubmem(mem_name);
    }
    int ptr_id = RunStat::instance()->shm_pubs[mem_name.c_str()]["ptr_id"].cast<int>();
    char* shm_ptr = RunStat::instance()->shm_ptrs[ptr_id];
    int shm_offset = RunStat::instance()->shm_pubs[mem_name.c_str()]["offset"].cast<int>();
    int shm_fst = RunStat::instance()->shm_pubs[mem_name.c_str()]["fst"].cast<int>();

    py::dict result;
    result["type"] = "memory_msgs::RawImage";
    result["encoding"] = encoding;
    result["shm_name"] = mem_name;
    result["height"] = h;
    result["width"] = w;
    // result["offset"] = 0;
    // result["shm_fst"] = 0;

    if (1 == shm_fst)
    {
        result["shm_fst"] = 1;
        RunStat::instance()->shm_pubs[mem_name.c_str()]["fst"] = 0;
    }
    else
    {
        result["shm_fst"] = 0;
    }

    int img_siz = h * w * tp * 2;  // cvimg.total() * cvimg.elemSize();
    if (shm_offset + img_siz > g_shm_size)
    {
        shm_offset = 0;
    }
    std::memcpy(shm_ptr + shm_offset, buf.ptr, img_siz);
    result["offset"] = shm_offset;
    RunStat::instance()->shm_pubs[mem_name.c_str()]["offset"] = static_cast<int>(shm_offset + img_siz);

    return result;
}


py::dict cvimg2sms_float(py::array_t<float> input, const std::string& mem_name)
{
    py::buffer_info buf = input.request();
    size_t ndim = input.ndim();
    const auto shape = input.shape();

    std::string encoding;
    int tp = 1;
    if (ndim == 2 || ndim == 3)
    {
        if (ndim == 2)
        {
            encoding = "32FC1";
            tp = 1;
        }
        else
        {
            if (shape[2] == 1)
            {
                encoding = "32FC1";
                tp = 1;
            }
            else if (shape[2] == 2)
            {
                encoding = "32FC2";
                tp = 2;
            }
            else if (shape[2] == 3)
            {
                encoding = "32FC3";
                tp = 3;
            }
            else if (shape[2] == 4)
            {
                encoding = "32FC4";
                tp = 4;
            }
            else
            {
                throw std::runtime_error("Unsupported sms::encoding type!");
            }
        }
    }
    else
    {
        throw std::runtime_error("Unsupported sms::encoding type!");
    }
    int h = shape[0];
    int w = shape[1];

    if (!RunStat::instance()->shm_pubs.contains(mem_name.c_str()))
    {
        init_pubmem(mem_name);
    }
    int ptr_id = RunStat::instance()->shm_pubs[mem_name.c_str()]["ptr_id"].cast<int>();
    char* shm_ptr = RunStat::instance()->shm_ptrs[ptr_id];
    int shm_offset = RunStat::instance()->shm_pubs[mem_name.c_str()]["offset"].cast<int>();
    int shm_fst = RunStat::instance()->shm_pubs[mem_name.c_str()]["fst"].cast<int>();

    py::dict result;
    result["type"] = "memory_msgs::RawImage";
    result["encoding"] = encoding;
    result["shm_name"] = mem_name;
    result["height"] = h;
    result["width"] = w;
    // result["offset"] = 0;
    // result["shm_fst"] = 0;

    if (1 == shm_fst)
    {
        result["shm_fst"] = 1;
        RunStat::instance()->shm_pubs[mem_name.c_str()]["fst"] = 0;
    }
    else
    {
        result["shm_fst"] = 0;
    }

    int img_siz = h * w * tp * 4;  // cvimg.total() * cvimg.elemSize();
    if (shm_offset + img_siz > g_shm_size)
    {
        shm_offset = 0;
    }
    std::memcpy(shm_ptr + shm_offset, buf.ptr, img_siz);
    result["offset"] = shm_offset;
    RunStat::instance()->shm_pubs[mem_name.c_str()]["offset"] = static_cast<int>(shm_offset + img_siz);

    return result;
}


void mem_cleanup(const std::string& mem_name)
{
    if (RunStat::instance()->shm_pubs.contains(mem_name.c_str()))
    {
        int ptr_id = RunStat::instance()->shm_pubs[mem_name.c_str()]["ptr_id"].cast<int>();
        char* shm_ptr = RunStat::instance()->shm_ptrs[ptr_id];
        int shm_fd = RunStat::instance()->shm_pubs[mem_name.c_str()]["fd"].cast<int>();

        RunStat::instance()->shm_pubs.attr("__delitem__")(mem_name.c_str());
        munmap(shm_ptr, g_shm_size);
        close(shm_fd);
        shm_unlink(mem_name.c_str());
    }
}


// 定义 Python 模块
PYBIND11_MODULE(csms_shm, m) {
    m.def("cvimg2sms_uint8", &cvimg2sms_uint8, "cv::Mat(CV_8U) to SpireMS image with shared memory");
    m.def("cvimg2sms_uint16", &cvimg2sms_uint16, "cv::Mat(CV_16U) to SpireMS image with shared memory");
    m.def("cvimg2sms_float", &cvimg2sms_float, "cv::Mat(CV_32F) to SpireMS image with shared memory");
    m.def("sms2cvimg_uint8", &sms2cvimg_uint8, "SpireMS image to cv::Mat(CV_8U) with shared memory");
    m.def("sms2cvimg_uint16", &sms2cvimg_uint16, "SpireMS image to cv::Mat(CV_16U) with shared memory");
    m.def("sms2cvimg_float", &sms2cvimg_float, "SpireMS image to cv::Mat(CV_32F) with shared memory");
    m.def("mem_cleanup", &mem_cleanup, "Clean up shared memory");
}

