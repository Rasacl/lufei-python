import redis

# 方式一
# r = redis.Redis(host='127.0.0.1', port=6379)
#
# r.set('xxx', 'yyyy')

# 方式二

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

r.set('bar', 'Foo')

print(r.get('bar'))