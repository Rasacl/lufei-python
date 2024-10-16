class Dog:
    d_type = '京巴'  # 属性 类属性， 类变量  公共属性

    def __init__(self, name, age):  # 初始化方法， 类方法， 构造方法 构造函数， 实例化时会自动进行一些初始化工作
        self.name = name  # 实例属性 私有化 绑定参数值到实例上
        self.age = age

    def say_hi(self):  # self 代表实例本身 第一个参数必须时self 否则会报错
        print('hello, I am a dog, my type is', self.d_type)


d = Dog('小黑', 2)  # 生成一个实例
print(d.d_type)
d.say_hi()


class People:
    nationality = '中国'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


p = People('小明', 18, '男')
print(People.nationality)
