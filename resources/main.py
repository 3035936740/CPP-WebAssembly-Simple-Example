import http.server
import socketserver
import os

# 设置端口号
PORT = 8000

# 定义处理请求的处理程序
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# 切换到你的项目目录，以确保能够找到 WasmCpp.wasm 文件
os.chdir('resources')

# 创建一个简单的 HTTP 服务器
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print("Serving at port", PORT)
    # 启动 HTTP 服务器，直到按下 Ctrl+C 终止
    httpd.serve_forever()
