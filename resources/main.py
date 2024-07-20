import http.server
import socketserver
import os

# ���ö˿ں�
PORT = 8080

# ���崦������Ĵ������
class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()

# �л��������ĿĿ¼����ȷ���ܹ��ҵ� WasmCpp.wasm �ļ�
os.chdir('resources')

# ����һ���򵥵� HTTP ������
with socketserver.TCPServer(("", PORT), HTTPRequestHandler) as httpd:
    print("Serving at port", PORT)
    # ���� HTTP ��������ֱ������ Ctrl+C ��ֹ
    httpd.serve_forever()
