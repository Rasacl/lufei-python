# 类方法通过@classmethod装饰器来修饰， 类方法与普通方法的区别是 类方法只能访问 类属性， 而普通方法可以访问类属性和实例属性。
class Dog(object):
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.count += 1

    @classmethod
    def get_count(cls):  # 在这里cls接收的不是实例本身， 而是类本身
        return cls.count


d = Dog("wangcai", 3)
print(Dog.get_count())
