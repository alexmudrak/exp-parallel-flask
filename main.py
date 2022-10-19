import asyncio
import time
from urllib import request

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message": "Hello, Flask!"})


def simple_consumer():
    # input("Press enter request... ")
    while True:
        request.urlopen("http://127.0.0.1:8000")
        print("Consume...")
        time.sleep(2)


async def start_flask():
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, app.run)


async def start_consumer():
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, simple_consumer)


async def start():
    await asyncio.gather(start_consumer(), start_flask())


if __name__ == "__main__":
    asyncio.run(start())
