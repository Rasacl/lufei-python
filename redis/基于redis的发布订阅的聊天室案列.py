import redis
import time

import threading

r = redis.Redis(host='127.0.0.1', port=6379)


def send_msg():
    msg = input('请输入要发送的消息：')
    r.publish('room_101', msg)


def recv_msg():
    # 创建 pubsub 对象并订阅频道
    pub = r.pubsub()
    pub.subscribe('room_101')

    pub.parse_response()
    # 消息监听循环
    while True:
        message = pub.get_message()
        if message:
            print(f"消息来啦: {message}")
        time.sleep(1)  # 为了防止过多的 CPU 占用，加入 sleep


threading.Thread(target=send_msg).start()


recv_msg()