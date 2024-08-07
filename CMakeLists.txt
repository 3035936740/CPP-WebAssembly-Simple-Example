cmake_minimum_required (VERSION 3.16)

project(WasmCpp)

# 设置项目根节点
set(PROJECT_ROOT_NODE ${CMAKE_CURRENT_SOURCE_DIR})

# 设置编译器
set(CMAKE_C_COMPILER emcc)
set(CMAKE_CXX_COMPILER em++)

# 指定 C++ 标准
set(CMAKE_CXX_STANDARD 17)
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

# LTO (Link Time Optimization) 是一种优化技术，它允许编译器在链接阶段进行优化。LTO 可以提高代码的性能和减少生成文件的大小
# -flto, -flto=full, -flto=thin: 这些是 LLVM 编译器的标志，用于启用不同类型的 LTO
# -flto: 启用标准 LTO
# -flto=full: 启用完整的 LTO
# -flto=thin: 启用薄 LTO（目前测试较少，因此建议使用标准 LTO）

# USE_PTHREADS=1: 启用 WebAssembly 线程支持
# USE_PTHREADS=0: 禁用 WebAssembly 线程支持（默认情况下也可以省略此设置）

# PTHREAD_POOL_SIZE=4 线程池大小

# 设置目标属性
set_target_properties(${PROJECT_NAME} PROPERTIES
    COMPILE_FLAGS "-flto -O3"
    LINK_FLAGS "-pthread -s USE_PTHREADS=1 -s PTHREAD_POOL_SIZE=4 -s WASM=1 -s EXPORTED_RUNTIME_METHODS=${EXPORTED_RUNTIME_METHODS} -flto" # -s EXPORTED_FUNCTIONS=${EXPORTED_FUNCTIONS}  --no-entry
    SUFFIX ".html"
)
