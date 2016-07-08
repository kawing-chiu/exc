cmake_minimum_required(VERSION 2.6)
project(Tutorial)

set(Tutorial_VERSION_MAJOR 1)
set(Tutorial_VERSION_MINOR 0)

#set(SOURCES src/tutorial.cpp)
file(GLOB SOURCES "src/*.cpp")

#configure_file(
#    "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
#    "${PROJECT_BINARY_DIR}/TutorialConfig.h"
#    )


include_directories(include)

add_executable(Tutorial ${SOURCES})
