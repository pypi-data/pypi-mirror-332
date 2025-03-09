cmake_minimum_required(VERSION 3.15...3.30)
project(flash_tokenizer VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Python and pybind11
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

# Add the C++ library
add_library(bert_tokenizer STATIC
    src/bert_tokenizer.cpp
)
target_include_directories(bert_tokenizer PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Add the Python module
pybind11_add_module(_core python/src/bindings.cpp)
target_link_libraries(_core PRIVATE bert_tokenizer)
target_compile_definitions(_core PRIVATE VERSION_INFO=${PROJECT_VERSION})

# Install the Python module
install(TARGETS _core DESTINATION flash_tokenizer)

# Add the executable (optional, for testing)
add_executable(FlashTokenizer main.cpp)
target_link_libraries(FlashTokenizer PRIVATE bert_tokenizer)
