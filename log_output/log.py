import string
import random
from datetime import datetime, time
from time import sleep 

def generate_log():
    log_string = string.ascii_letters
    log = ''.join(random.choice(log_string) for _ in range(32))
    return log

def log_time():
    date_log = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return date_log

while True:
     print (log_time() + ": " + generate_log(), flush=True)
     sleep(5)
