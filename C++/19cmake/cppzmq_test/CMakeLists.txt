cmake_minimum_required(VERSION 3.5)
project(zmq_test)

set(CMAKE_C_VISIBILITY_PRESET hidden)
set(CMAKE_CXX_VISIBILITY_PRESET hidden)

message("PROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}")
message("PROJECT_BINARY_DIR=${PROJECT_BINARY_DIR}")

find_library(ZMQ_LIB libzmq)

add_executable(test_zmq test_zmq.cpp)

target_link_libraries(test_zmq ${ZMQ_LIB})
