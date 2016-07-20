
message("subdir-PROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}")
message("subdir-PROJECT_BINARY_DIR=${PROJECT_BINARY_DIR}")
message("subdir-CMAKE_CURRENT_SOURCE_DIR=${CMAKE_CURRENT_SOURCE_DIR}")
message("subdir-CMAKE_CURRENT_BINARY_DIR=${CMAKE_CURRENT_BINARY_DIR}")


set(exe_list "")
macro(_add_exe target srcs)
    add_executable(${target} ${srcs})
    target_link_libraries(${target} ${ZMQ_LIB})
    # if using static linking:
    #target_link_libraries(${target} ${ZMQ_LIB}
    #    -Wl,-Bstatic -lstdc++ -lpthread -Wl,-Bdynamic)
    list(APPEND exe_list ${target})
endmacro()

_add_exe(test_client client.cpp)
_add_exe(test_server server.cpp)
message("exe_list=${exe_list}")

install(TARGETS ${exe_list} DESTINATION bin)

#add_executable(test_client client.cpp)
#if(UNIX)
#    target_link_libraries(test_client ${ZMQ_LIB} -lpthread)
#else()
#    target_link_libraries(test_client ${ZMQ_LIB}
#        -Wl,-Bstatic -lstdc++ -lpthread -Wl,-Bdynamic)
#endif()

#add_executable(test_server server.cpp)
#if(UNIX)
#    target_link_libraries(test_server ${ZMQ_LIB} -lpthread)
#else()
#    target_link_libraries(test_server ${ZMQ_LIB}
#        -Wl,-Bstatic -lstdc++ -lpthread -Wl,-Bdynamic)
#endif()
