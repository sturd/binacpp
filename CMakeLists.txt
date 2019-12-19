cmake_minimum_required(VERSION 3.1)

project(binacpp)

include(conanbuildinfo.cmake)
conan_basic_setup()

if(UNIX)
    add_compile_options(-fPIC)
endif()

set(
    BINACPP_SOURCES
    src/binacpp_utils.cpp
    src/binacpp_logger.cpp
    src/binacpp_websocket.cpp
    src/binacpp.cpp
)

set(
    BINACPP_HEADERS
    src/binacpp_utils.h
    src/binacpp_logger.h
    src/binacpp_websocket.h
    src/binacpp.h
)

add_library(binacpp SHARED ${BINACPP_SOURCES} ${BINACPP_HEADERS})
target_link_libraries(
    binacpp
    jsoncpp
    $<$<PLATFORM_ID:Windows>:libcurl>
    websockets$<$<PLATFORM_ID:Windows>:_static>
)