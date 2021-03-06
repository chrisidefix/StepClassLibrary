
set(LIBSTEPUTILS_SRCS
    Str.cc 
    dirobj.cc 
    gennode.cc 
    gennodelist.cc 
    gennodearray.cc 
    scl_hash.cc 
    errordesc.cc 
)

SET(LIBSTEPUTILS_PRIVATE_HDRS
    dirobj.h 
    errordesc.h 
    gennodearray.h 
    gennode.h 
    gennodelist.h 
    scldir.h 
    scl_hash.h 
    stat.h 
    Str.h 
    str_list.h
)

include_directories(
    ${SCL_BINARY_DIR}/include
    ${CMAKE_CURRENT_SOURCE_DIR}
)

if (MSVC OR BORLAND)
add_definitions( -DSCL_UTILS_DLL_EXPORTS )
endif()

SCL_ADDLIB(steputils "${LIBSTEPUTILS_SRCS}" "")

IF(MINGW)
    TARGET_LINK_LIBRARIES(steputils shlwapi.lib)
ENDIF(MINGW)

IF(MSVC OR BORLAND)
	TARGET_LINK_LIBRARIES(steputils shlwapi.lib)
ENDIF()

if(APPLE)
    if(SCL_BUILD_SHARED_LIBS)
        set_target_properties(steputils PROPERTIES LINK_FLAGS "-flat_namespace -undefined suppress")
    endif(SCL_BUILD_SHARED_LIBS)
endif(APPLE)
