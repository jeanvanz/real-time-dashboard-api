import redis
from config.redis_config import REDIS_CONFIG

r = redis.Redis(**REDIS_CONFIG)

success = r.set('foo', 'bar')

result = r.get('foo')
print(result)