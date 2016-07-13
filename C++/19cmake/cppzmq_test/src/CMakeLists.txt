
message("subdir-PROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}")
message("subdir-PROJECT_BINARY_DIR=${PROJECT_BINARY_DIR}")
message("subdir-CMAKE_CURRENT_SOURCE_DIR=${CMAKE_CURRENT_SOURCE_DIR}")
message("subdir-CMAKE_CURRENT_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR}")



add_executable(test_client client.cpp)
target_link_libraries(test_client ${ZMQ_LIB})

add_executable(test_server server.cpp)
target_link_libraries(test_server ${ZMQ_LIB})
