from http.server import HTTPServer, BaseHTTPRequestHandler
import os


port = os.environ.get('PORT', 8000) 
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = f"<html><body><h1>Hello from port {port}!</h1></body></html>"
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
   
def run():
        server_address = ('', int(port))
        httpd = HTTPServer(server_address, MyHandler)
        print(f'Starting server on port {port}', flush=True)
        httpd.serve_forever()
if __name__ == "__main__":
    run()
