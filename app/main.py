import asyncio
import tornado.websocket
import tornado.web
from websocket_handler import WebSocketHandler

def make_app():
    return tornado.web.Application([
        (r"/ws", WebSocketHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888, address="0.0.0.0")
    print("Server rodando")

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())