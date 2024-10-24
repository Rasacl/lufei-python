import time
import uuid

import redis
import threading

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=3, decode_responses=True)
r = redis.Redis(connection_pool=pool)


def delayTask(name, delayTime):
    task_id = str(uuid.uuid4())

    processTime = time.time() + delayTime

    r.zadd('delay-queue', {name + task_id: processTime})


def loop():
    while 1:
        task_list = r.zrangebyscore('delay-queue', 0, time.time(), 0, 1)
        if not task_list:
            print('const 1秒')
            time.sleep(1)
            continue
        task_id = task_list[0]
        ok = r.zrem('delay-queue', task_id)
        if ok:
            handle_task(task_id)


def handle_task(task_id):
    print('开始处理任务：%s' % task_id)


t = threading.Thread(target=loop)
t.start()

delayTask('任务一', 5)
delayTask('任务二', 3)
delayTask('任务三', 10)
delayTask('任务四', 7)
