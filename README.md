# C++20 WebAssembly Example

This is a simple example demonstrating how to compile and build a C++20 program to WebAssembly (Wasm) using cmake and em++.

## Project Structure

Assume the project structure is as follows:

<pre><code>WasmExample
©¦
©À©¤©¤ CMakeLists.txt
©À©¤©¤ src
©¦   ©¸©¤©¤ main.cpp
©¸©¤©¤ resources
    ©À©¤©¤ main.py
    ©¸©¤©¤ resources
        ©¸©¤©¤ index.html</code></pre>

## Getting Started
### Clone the Repository
 ```bash
$ git clone https://github.com/3035936740/WebAssembly-Simple-Example.git
$ cd WebAssembly-Simple-Example
```  

### Build the Project
1. Create a Build Directory:  
 ```bash
$ mkdir build
$ cd build
```  

2. Compile and Build:  
 ```bash
$ cmake ..
$ cmake --build .
```  
This will generate WasmCpp.html, WasmCpp.js, and WasmCpp.wasm files in the bin/resources directory.

### Running the Example
#### Using Python HTTP Server
Navigate to the bin directory and start a Python HTTP server:
 ```bash
$ cd bin
$ python3 main.py
```  

#### Using emrun
Alternatively, you can run the HTML file using emrun:
 ```bash
$ cd bin/resources
$ emrun --no_browser --port 8080 --log_stdout stdout --log_stderr stderr ./index.html
```  

### Accessing the WebAssembly Example
Once the server is running, you can access the WebAssembly example at:
* http://localhost:8080/
* http://localhost:8080/WasmCpp.html

Ensure that WasmCpp.html, WasmCpp.js, and WasmCpp.wasm are correctly generated in the bin/resources directory. Adjust paths and port numbers as needed.