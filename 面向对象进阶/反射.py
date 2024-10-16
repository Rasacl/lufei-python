# 反射 可以通过字符串的形式来操作对象的属性、方法等

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("zhangsan", 18)

if hasattr(p, "age"): # 判断对象中是否存在age属性
    print("存在age属性")


# 反射、映射、自省
# getattr() # 获取对象属性
print(getattr(p, "age"))
# setattr() # 设置对象属性 static属性
setattr(p, "sex", "Male")
print(p.sex)
# delattr() # 删除对象属性
delattr(p, "age")
# hasattr() # 判断对象中是否存在属性
print(hasattr(p, "age"))