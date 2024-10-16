class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self, food):
        print(self.name, '正在吃', food)

    def sleep(self):
        print(self.name, '正在睡觉')

    def run(self):
        print(self.name, '正在跑')

    def play(self):
        print(self.name, '正在玩')


class Person(Animal):  # 继承Animal
    def __init__(self, name, age, sex, hobby):  # 重写父类的构造方法
        # Animal.__init__(self, name, age, sex)
        # super(Person, self).__init__(name, age, sex)
        super().__init__(name, age, sex)
        self.hobby = hobby

    def talk(self):
        print(self.name, '正在说话', self.hobby)

    def eat(self, food):  # 覆盖父类的方法
        print(self.name, '正在优雅的', food)


class Dog(Animal):  # 继承Animal
    def chase_rabbit(self):
        print(self.name, '正在追打小兔子')


p = Person('小明', 18, '男', '打游戏')
p.eat('大餐')
p.talk()

d = Dog('旺财', 3, '男')
d.eat('骨头')
d.chase_rabbit()
