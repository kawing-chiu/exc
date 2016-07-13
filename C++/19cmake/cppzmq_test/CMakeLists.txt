cmake_minimum_required(VERSION 3.5)
project(zmq_test)

set(CMAKE_C_VISIBILITY_PRESET hidden)
set(CMAKE_CXX_VISIBILITY_PRESET hidden)

message("PROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}")
message("PROJECT_BINARY_DIR=${PROJECT_BINARY_DIR}")
message("CMAKE_CURRENT_SOURCE_DIR=${CMAKE_CURRENT_SOURCE_DIR}")
message("CMAKE_CURRENT_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR}")

if(WIN32)
    set(platform win)
elseif(CMAKE_SYSTEM_NAME MATCHES Linux)
    set(platform linux)
else()
    message(FATAL_ERROR "Unsupported platform: '${CMAKE_SYSTEM_NAME}'")
endif()

if(CMAKE_SIZEOF_VOID_P EQUAL 8)
    set(bitsize 64)
elseif(CMAKE_SIZEOF_VOID_P EQUAL 4)
    set(bitsize 32)
else()
    message(FATAL_ERROR
        "Unknown CMAKE_SIZEOF_VOID_P: ${CMAKE_SIZEOF_VOID_P}")
endif()

set(arch_lib_dir "${platform}${bitsize}")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}")


find_library(ZMQ_LIB zmq)
message("ZMQ_LIB=${ZMQ_LIB}")

#include_directories("${PROJECT_SOURCE_DIR}/vendor/include/")
add_subdirectory("${PROJECT_SOURCE_DIR}/src")

