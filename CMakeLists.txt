cmake_minimum_required(VERSION 3.1)

project(binacpp)

include(conanbuildinfo.cmake)

set(OPENSSL_ROOT_DIR ${CONAN_OPENSSL_ROOT})
find_package(OpenSSL REQUIRED)

set(CURL_LIBRARY ${CONAN_LIBCURL_ROOT})
find_package(CURL REQUIRED)

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

add_library(binacpp STATIC ${BINACPP_SOURCES} ${BINACPP_HEADERS})
target_link_libraries(
    binacpp
    jsoncpp
    $<$<PLATFORM_ID:Windows>:libcurl>
    websockets$<$<PLATFORM_ID:Windows>:_static>
    CURL::libcurl
    dl
    z
    OpenSSL::SSL
    OpenSSL::Crypto
)