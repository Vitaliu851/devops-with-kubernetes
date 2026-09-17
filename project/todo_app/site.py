from http.server import HTTPServer, BaseHTTPRequestHandler
import os


port = os.environ.get('PORT', 8000) 
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Ок'.encode('utf-8'))
def run():
        server_address = ('', int(port))
        httpd = HTTPServer(server_address, MyHandler)
        print(f'Starting server on port {port}', flush=True)
        httpd.serve_forever()
if __name__ == "__main__":
    run()
