import time
from multiprocessing import Process
from urllib import request

from main import app


def run():
    while True:
        request.urlopen("http://127.0.0.1:8000")
        time.sleep(5)


t = Process(target=run)
t.start()
app
