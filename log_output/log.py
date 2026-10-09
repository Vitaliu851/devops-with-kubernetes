import string
import random
import threading
from datetime import datetime, time
from time import sleep 
from http.server import HTTPServer, BaseHTTPRequestHandler
latest_time = ""
latest_string = ""
PORT = 3002

def generate_log():
    log_string = string.ascii_letters
    return ''.join(random.choice(log_string) for _ in range(32))

def log_time():
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")

def background_logger():
    global latest_time, latest_string
    while True:
        latest_time = log_time()
        latest_string = generate_log()
        print(f"{latest_time}: {latest_string}", flush=True)
        sleep(5)

class StatusHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            response_text = f"{latest_time}: {latest_string}\n"

            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(response_text.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        return

def run():
    t = threading.Thread(target=background_logger, daemon=True)
    t.start()

    server_address = ('', PORT)
    httpd = HTTPServer(server_address, StatusHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
