import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# 字符串操作
r.set('bar', 'Foo')
print(r.get('bar'))

# 不允许对已经存在的键设置值
ret = r.setnx('name', 'yuan')
print(ret)

# 设置有效期
r.setex('good_1001', 10, '2')

# 字符串操作 自增自减
r.set('age', 20)
r.incrby('age', 5)
print(r.get('age'))

# hash操作 设置hash

r.hset('info', 'name', 'ran')
