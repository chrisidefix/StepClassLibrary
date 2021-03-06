
set(LIBSTEPEDITOR_SRCS
    STEPfile.cc 
    STEPfile.inline.cc 
    cmdmgr.cc 
    dispnode.cc 
    dispnodelist.cc 
    instmgr.cc 
    mgrnode.cc 
    mgrnodearray.cc 
    mgrnodelist.cc 
    needFunc.cc 
    SdaiHeaderSchema.cc
    SdaiHeaderSchemaAll.cc
    SdaiHeaderSchemaInit.cc
    SdaiSchemaInit.cc
)

SET(LIBSTEPEDITOR_PRIVATE_HDRS
    STEPfile.h 
    cmdmgr.h 
    dispnode.h 
    dispnodelist.h 
    editordefines.h 
    instmgr.h 
    mgrnode.h 
    mgrnodearray.h 
    mgrnodelist.h 
    needFunc.h 
    SdaiHeaderSchema.h
    SdaiHeaderSchemaClasses.h
    SdaiSchemaInit.h
    seeinfodefault.h
)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${SCL_SOURCE_DIR}/src/cldai
    ${SCL_SOURCE_DIR}/src/clstepcore
    ${SCL_SOURCE_DIR}/src/clutils
)

if(MSVC OR BORLAND)
add_definitions( -DSCL_EDITOR_DLL_EXPORTS )
add_definitions( -DSCL_CORE_DLL_IMPORTS )
add_definitions( -DSCL_DAI_DLL_IMPORTS )
add_definitions( -DSCL_UTILS_DLL_IMPORTS )
endif()

SCL_ADDLIB(stepeditor "${LIBSTEPEDITOR_SRCS}" stepcore stepdai steputils)

if(APPLE)
    if(SCL_BUILD_SHARED_LIBS)
        set_target_properties(stepeditor PROPERTIES LINK_FLAGS "-flat_namespace -undefined suppress")
    endif(SCL_BUILD_SHARED_LIBS)
endif(APPLE)
