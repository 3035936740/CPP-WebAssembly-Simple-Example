# C++20 WebAssembly Example

This is a simple example demonstrating how to compile and build a C++20 program to WebAssembly (Wasm) using cmake and em++.

### Project Structure

Assume the project structure is as follows:

<pre><code>WasmExample
------ CMakeLists.txt  
------ src  
       ------ main.cpp  
------ main.cpp  
------ resources  
       ------main.py  
       ------resources  
             ------index.html  
</code></pre>

1. **Clone the Repository:**  
 ```bash
$ git clone https://github.com/3035936740/WebAssembly-Simple-Example.git
$ cd WebAssembly-Simple-Example
```  

2. Create a Build Directory:  
 ```bash
$ mkdir build
$ cd build
```  

3. Compile and Build:  
 ```bash
$ cmake ..
$ cmake --build .
```  
This will generate WasmCpp.html, WasmCpp.js, and WasmCpp.wasm files in the bin/resources directory.

### Running the Example
Navigate to the bin directory and start a Python HTTP server:
 ```bash
$ cd bin
$ python3 main.py
```  
Then, you can access the WebAssembly example at:  
* http://localhost:8000/
* http://localhost:8000/WasmCpp.html

This setup assumes your WasmCpp.html, WasmCpp.js, and WasmCpp.wasm files are correctly generated in the bin/resources directory as configured in your CMakeLists.txt. Adjust the paths and port number as needed based on your setup.
