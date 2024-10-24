import redis
import time

# 连接到 Redis
r = redis.Redis(host='localhost', port=6379)

# 创建 pubsub 对象并订阅频道
pub = r.pubsub()
pub.subscribe('room_101')

pub.parse_response()
# 消息监听循环
while True:
    print('waiting......')
    message = pub.get_message()
    if message:
        print(f"消息来啦: {message}")
    time.sleep(1)  # 为了防止过多的 CPU 占用，加入 sleep
