class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__life_val = 100  # 私有属性

    def get_life_val(self):
        return self.__life_val

    def __set_life_val(self, val): # 私有方法
        self.__life_val = val


p = Person('小明', 18)
# p.life_val -= 10
print(p.get_life_val())
