from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import time
import getpass

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        user = getpass.getuser()
        host_ip = self.client_address[0]
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        response_text = f'Hello world from hostname: {socket.gethostname()}, Current Time: {current_time}, ' \
                        f'username: {user}, server IP: {host_ip}'
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response_text.encode())

SERVER_PORT = 8000
httpd = HTTPServer(('0.0.0.0', SERVER_PORT), SimpleHTTPRequestHandler)
print('Listening on port %s ...' % SERVER_PORT)
httpd.serve_forever()
