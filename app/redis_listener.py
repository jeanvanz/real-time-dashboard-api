import redis
import asyncio
from config.redis_config import REDIS_CONFIG

class RedisListener:
    def __init__(self):
        self.redis_client = redis.Redis(**REDIS_CONFIG)
        self.pubsub = self.redis_client.pubsub()
        self.pubsub.subscribe('real_time_dashboard')
        print("Redis listener inicializado e inscrito no canal 'real_time_dashboard'")
    
    async def listen_for_messages(self, callback):
        print("Iniciando escuta de mensagens do Redis...")
        
        while True:
            try:
                message = self.pubsub.get_message(timeout=1.0)
                
                if message and message['type'] == 'message':
                    data = message['data']
                    
                    if isinstance(data, bytes):
                        data = data.decode('utf-8')
                    
                    print(f"Mensagem recebida do Redis: {data}")
                    
                    if callback:
                        await callback(data)
                
                await asyncio.sleep(0.1)
                
            except Exception as e:
                print(f"Erro no listener Redis: {e}")
                await asyncio.sleep(1)
    
    def close(self):
        if self.pubsub:
            self.pubsub.close()
        if self.redis_client:
            self.redis_client.close()
        print("Conexão Redis fechada")