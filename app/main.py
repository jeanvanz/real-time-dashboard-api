import asyncio
import tornado.websocket
import tornado.web
from websocket_handler import WebSocketHandler
from redis_listener import redisListener

def read_send_data():
    data = redisListener()
    print(data)

def make_app():
    return tornado.web.Application([
        (r"/ws", WebSocketHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888, address="0.0.0.0")
    print("Server rodando")
    read_send_data()

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())