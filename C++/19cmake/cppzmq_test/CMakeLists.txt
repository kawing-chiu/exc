cmake_minimum_required(VERSION 3.5)
project(zmq_test)

message("CMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}")
message("CMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}")
message("PROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}")
message("PROJECT_BINARY_DIR=${PROJECT_BINARY_DIR}")
message("CMAKE_CURRENT_SOURCE_DIR=${CMAKE_CURRENT_SOURCE_DIR}")
message("CMAKE_CURRENT_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR}")

# test for platform
if(WIN32)
    set(platform win)
    if(NOT MINGW)
        message(FATAL_ERROR "Only mingw is supported on windows")
    endif()
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
message("arch_lib_dir: ${arch_lib_dir}")
message("MINGW=${MINGW}")
if(MINGW)
    get_filename_component(mingw_path ${CMAKE_CXX_COMPILER} DIRECTORY)
    message("mingw_path=${mingw_path}")
endif()


# add include directories and compiler/linker flags
set(CMAKE_C_VISIBILITY_PRESET hidden)
set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
add_compile_options(-pthread)
if(MINGW)
    #set(link_flags "-static-libgcc -static-libstdc++ -Wl,-verbose")
    #set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${link_flags}")
    message("CMAKE_CXX_FLAGS=${CMAKE_CXX_FLAGS}")
    message("CMAKE_EXE_LINKER_FLAGS=${CMAKE_EXE_LINKER_FLAGS}")
    message("CMAKE_SYSTEM_PREFIX_PATH=${CMAKE_SYSTEM_PREFIX_PATH}")
    message("CMAKE_SYSTEM_LIBRARY_PATH=${CMAKE_SYSTEM_LIBRARY_PATH}")
    message("CMAKE_FIND_LIBRARY_SUFFIXES=${CMAKE_FIND_LIBRARY_SUFFIXES}")
endif()
include_directories("${PROJECT_SOURCE_DIR}/vendor/include/")

# finding necessary libraries
if(UNIX)
    find_library(ZMQ_LIB zmq)
else()
    set(lib_list "")
    macro(_find_lib var lib)
        find_library(${var} ${lib})
        list(APPEND lib_list ${${var}})
    endmacro()

    set(default_library_suffixes ${CMAKE_FIND_LIBRARY_SUFFIXES})
    set(CMAKE_FIND_LIBRARY_SUFFIXES .dll)
    # manually specify all dependencies
    _find_lib(ZMQ_LIB zmq)
    _find_lib(PTHREAD_LIB winpthread-1)
    _find_lib(GCC_LIB gcc_s_dw2-1)
    _find_lib(C++_LIB stdc++-6)
    _find_lib(SODIUM_LIB sodium-18)
    message("lib_list=${lib_list}")
    set(CMAKE_FIND_LIBRARY_SUFFIXES ${default_library_suffixes})
endif()
message("ZMQ_LIB=${ZMQ_LIB}")
message("PTHREAD_LIB=${PTHREAD_LIB}")
message("GCC_LIB=${GCC_LIB}")
message("C++_LIB=${C++_LIB}")
message("SODIUM_LIB=${SODIUM_LIB}")

# not working on mingw:
#find_package(Threads REQUIRED)
#message("CMAKE_THREAD_LIBS_INIT=${CMAKE_THREAD_LIBS_INIT}")

# set output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/bin")

# copy libs target for windows
if(MINGW)
    set(dlls_to_copy ${lib_list})
    add_custom_target(copy_dlls ALL)
    add_custom_command(TARGET copy_dlls POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_if_different
        ${dlls_to_copy}
        ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}
    )
    install(FILES ${dlls_to_copy} DESTINATION bin)
endif()

# add subdirectories
add_subdirectory("${PROJECT_SOURCE_DIR}/src")

# cpack
#include(InstallRequiredSystemLibraries)
#message("CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS=${CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS}")
include(CPack)



