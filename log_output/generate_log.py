import string
import random
from datetime import datetime, time
from time import sleep 

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
        with open("/log/log.txt", "a+") as file:
            file.write(f"{latest_time}: {latest_string}\n")
        sleep(5)
if __name__ == "__main__":
    background_logger()

