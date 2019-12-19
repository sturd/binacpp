#ifndef BINACPP_EXPORT_H
#define BINACPP_EXPORT_H

#if defined(_MSC_VER)
    //  Microsoft 
    #define LIB_EXPORT __declspec(dllexport)
    #define LIB_IMPORT __declspec(dllimport)
#elif defined(__GNUC__)
    //  GCC
    #define LIB_EXPORT __attribute__((visibility("default")))
    #define LIB_IMPORT
#else
    //  do nothing and hope for the best?
    #define LIB_EXPORT
    #define LIB_IMPORT
    #pragma warning Unknown dynamic link import/export semantics.
#endif

#ifdef EXPORT_BINACPP_SYMBOLS
    #define BINCPP_EXPORT LIB_EXPORT
#else
    #define BINACPP_EXPORT LIB_IMPORT
#endif

#endif // BINACPP_EXPORT_H