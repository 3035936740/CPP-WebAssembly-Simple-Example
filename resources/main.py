import http.server
import socketserver
import os

# ���ö˿ں�
PORT = 8000

# ���崦������Ĵ������
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# �л��������ĿĿ¼����ȷ���ܹ��ҵ� WasmCpp.wasm �ļ�
os.chdir('resources')

# ����һ���򵥵� HTTP ������
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print("Serving at port", PORT)
    # ���� HTTP ��������ֱ������ Ctrl+C ��ֹ
    httpd.serve_forever()
