cmake_minimum_required (VERSION 3.16)

project(WasmCpp)

# 设置项目根节点
set(PROJECT_ROOT_NODE ${CMAKE_CURRENT_SOURCE_DIR})

# 设置编译器
set(CMAKE_C_COMPILER emcc)
set(CMAKE_CXX_COMPILER em++)

# 指定 C++ 标准
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# 定义导出函数列表
set(EXPORTED_FUNCTIONS '[\"_say_hello\",\"_reversenumber\"]')

# 定义导出的 Emscripten 运行时方法
set(EXPORTED_RUNTIME_METHODS "ccall,cwrap")

# 将指定目录文件所有复制到二进制文件目录
file(GLOB allCopyFiles  "${PROJECT_ROOT_NODE}/resources/*")
file(COPY ${allCopyFiles} DESTINATION ${PROJECT_ROOT_NODE}/bin)

# 指定最终的可执行文件的位置
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_ROOT_NODE}/bin/resources)

# 以当前目录为基准
include_directories(${PROJECT_ROOT_NODE}/src)

# 将源代码添加到此项目的可执行文件。
# aux_source_directory(${PROJECT_ROOT_NODE}/src SRC_LIST)
set(SOURCES ${PROJECT_ROOT_NODE}/src/main.cpp)

add_executable(${PROJECT_NAME} ${SOURCES})

# 设置目标属性
set_target_properties(${PROJECT_NAME} PROPERTIES
    LINK_FLAGS "-s WASM=1 -s EXPORTED_RUNTIME_METHODS=${EXPORTED_RUNTIME_METHODS} --no-entry" # -s EXPORTED_FUNCTIONS=${EXPORTED_FUNCTIONS} 
    SUFFIX ".html"
)
