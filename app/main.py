import asyncio
import tornado.websocket
import tornado.web
import redis
from websocket_handler import WebSocketHandler

def redis_listener():
    r = redis.Redis(
    host='redis-17263.c10.us-east-1-4.ec2.redns.redis-cloud.com',
    port=17263,
    password='MtAMMqqMoWwrmwe6bvmQ9b38Sj4yA4Yj',
    ssl=False
)
    pubsub = r.pubsub()
    pubsub.subscribe('real_time_dashboard')
    
    for message in pubsub.listen():
        if message and message['type'] == 'message':
            data = message['data']
            print(data)

def make_app():
    return tornado.web.Application([
        (r"/ws", WebSocketHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888, address="0.0.0.0")
    redis_listener()
    print("Server rodando")

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())