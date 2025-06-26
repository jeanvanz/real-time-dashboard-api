import redis
import psutil
import time
import json

r = redis.Redis(
    host='redis-17263.c10.us-east-1-4.ec2.redns.redis-cloud.com',
    port=17263,
    password='MtAMMqqMoWwrmwe6bvmQ9b38Sj4yA4Yj',
    ssl=False
)

while True:
    data = {
        'cpu': psutil.cpu_percent(),
        'ram': psutil.virtual_memory().percent
    }
    r.publish('real_time_dashboard', json.dumps(data))
    print(data)
    time.sleep(1)
