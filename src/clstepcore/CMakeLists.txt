
set(LIBSTEPCORE_SRCS
    sdaiApplication_instance.cc 
    STEPcomplex.cc 
    STEPattribute.cc 
    STEPattribute.inline.cc 
    sdai.cc 
    sdaiSelect.cc 
    STEPaggregate.cc 
    STEPundefined.cc 
    STEPattributeList.cc 
    SingleLinkList.cc 
    SingleLinkList.inline.cc 
    Registry.inline.cc 
    ExpDict.cc 
    ExpDict.inline.cc 
    read_func.cc 
    collect.cc 
    complexlist.cc 
    entlist.cc 
    multlist.cc 
    orlist.cc 
    entnode.cc 
    non-ors.cc 
    match-ors.cc 
    trynext.cc 
    print.cc
)

if(MINGW)
	set(LIBDEPEND_SRCS
		${SCL_SOURCE_DIR}/src/cleditor/instmgr.cc
		${SCL_SOURCE_DIR}/src/cleditor/mgrnode.cc
		${SCL_SOURCE_DIR}/src/cleditor/dispnode.cc
		${SCL_SOURCE_DIR}/src/cleditor/mgrnodearray.cc
		${SCL_SOURCE_DIR}/src/cleditor/needFunc.cc
	)
endif(MINGW)

if(MSVC OR BORLAND)
	set(LIBDEPEND_SRCS
		${SCL_SOURCE_DIR}/src/cleditor/instmgr.cc
		${SCL_SOURCE_DIR}/src/cleditor/mgrnode.cc
		${SCL_SOURCE_DIR}/src/cleditor/dispnode.cc
		${SCL_SOURCE_DIR}/src/cleditor/mgrnodearray.cc
		${SCL_SOURCE_DIR}/src/cleditor/needFunc.cc
	)
endif()

if(MSVC OR BORLAND)
	add_definitions( -DSCL_CORE_DLL_EXPORTS )
	add_definitions( -DSCL_EXPRESS_DLL_IMPORTS )
	add_definitions( -DSCL_UTILS_DLL_IMPORTS )
	add_definitions( -DSCL_DAI_DLL_IMPORTS )
endif()

SET(LIBSTEPCORE_PRIVATE_HDRS
    baseType.h 
    complexSupport.h 
    dictdefs.h 
    ExpDict.h 
    read_func.h 
    Registry.h 
    sdaiApplication_instance.h 
    sdaiBinary.h 
    sdaiEnum.h 
    sdai.h 
    sdaiSelect.h 
    sdaiString.h 
    Select.h 
    SingleLinkList.h 
    STEPaggregate.h 
    STEPattribute.h 
    STEPattributeList.h 
    STEPcomplex.h 
    STEPundefined.h
)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${SCL_SOURCE_DIR}/src/cldai
    ${SCL_SOURCE_DIR}/src/cleditor
    ${SCL_SOURCE_DIR}/src/clutils
)

SCL_ADDLIB(stepcore "${LIBSTEPCORE_SRCS} ${LIBDEPEND_SRCS}" "express steputils stepdai")
if(APPLE)
    if(SCL_BUILD_SHARED_LIBS)
        set_target_properties(stepcore PROPERTIES LINK_FLAGS "-flat_namespace -undefined suppress")
    endif(SCL_BUILD_SHARED_LIBS)
endif(APPLE)
