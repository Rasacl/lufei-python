import redis
import time

# 连接到 Redis
r = redis.Redis(host='localhost', port=6379)

# 创建 pubsub 对象并发布频道
r.publish('room_101', 'Hello, world!')

