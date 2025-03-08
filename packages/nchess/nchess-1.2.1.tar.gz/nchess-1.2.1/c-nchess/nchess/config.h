/*
    config.h

    This file contains the configuration macros for the project.
    The macros are used to define the inline functions, static functions.
*/

#ifndef NCHESS_SRC_CONFIG_H
#define NCHESS_SRC_CONFIG_H

#define NCH_STATIC static

#if defined(__GNUC__)
    #define NCH_GCC 1
    #define NCH_CLANG 0
    #define NCH_MSC 0
#elif defined(__clang__)
    #define NCH_GCC 0
    #define NCH_CLANG 1
    #define NCH_MSC 0
#elif defined(_MSC_VER)
    #define NCH_GCC 0
    #define NCH_CLANG 0
    #define NCH_MSC 1
#endif

#if defined(__GNUC__) || defined(__clang__)  // GCC and Clang
    #define NCH_INLINE __inline__
    #define NCH_NOINLINE __attribute__((noinline))
    #define NCH_FINLINE __attribute__((always_inline)) __inline__
    #define NCH_TLS __thread
#elif defined(_MSC_VER)  // Microsoft Visual Studio Compiler
    #define NCH_INLINE __inline
    #define NCH_NOINLINE __declspec(noinline)
    #define NCH_FINLINE __forceinline
    #define NCH_TLS __declspec(thread)
#endif

#define NCH_STATIC_INLINE NCH_STATIC NCH_INLINE
#define NCH_STATIC_FINLINE NCH_STATIC NCH_FINLINE

#if defined(__GNUC__) || defined(__ICC) || defined(__clang__)
    #define NCH_UNUSED(x) __attribute__((unused)) x
#elif defined(_MSC_VER)
    #define NCH_UNUSED(x) __pragma(warning(suppress: 4100)) x
#else
    #define NCH_UNUSED(x) x
#endif


#endif // NCHESS_SRC_CONFIG_H