class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self): # 获取长度
        return self.age

    def __hash__(self): # 获取hash值
        return hash(p.name)

    def __eq__(self, other): # 比较
        return self.name == other.name

p = Person("小明", 18)
print(len(p))
print(hash(p))