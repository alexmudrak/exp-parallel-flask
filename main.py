import asyncio

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


def simple_consumer():
    input("Press enter request... ")


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
