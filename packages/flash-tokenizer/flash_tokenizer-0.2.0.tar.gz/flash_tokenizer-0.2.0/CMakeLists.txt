cmake_minimum_required(VERSION 3.15)
project(flash_tokenizer VERSION 0.2.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

add_library(bert_tokenizer STATIC
        src/bert_tokenizer.cpp
)
target_include_directories(bert_tokenizer PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)


pybind11_add_module(_core python/src/bindings.cpp)
target_link_libraries(_core PRIVATE bert_tokenizer)
target_compile_definitions(_core PRIVATE VERSION_INFO=${PROJECT_VERSION})


install(TARGETS _core DESTINATION flash_tokenizer)


#target_include_directories(FlashTokenizer PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
#add_executable(FlashTokenizer main.cpp src/bert_tokenizer.cpp include/bert_tokenizer.h)
#target_link_libraries(FlashTokenizer PRIVATE bert_tokenizer)
