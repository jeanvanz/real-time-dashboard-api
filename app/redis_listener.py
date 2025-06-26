import redis
from config.redis_config import REDIS_CONFIG

# def redisListener():
#     data = 'preciso pescar'
#     return data

def redisListener():
    r = redis.Redis(**REDIS_CONFIG)
    pubsub = r.pubsub()
    pubsub.subscribe('real_time_dashboard')
    
    for message in pubsub.listen():
        if message and message['type'] == 'message':
            data = message['data']
            
            return data

