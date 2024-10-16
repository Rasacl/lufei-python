# 由一堆组件构成一个完整的个体，组件本身独立，但又不能自己独立运行，必须和宿主组合在一起，运行
class Dog:
    role = "dog"

    def __init__(self, name, breed, attack_val,life_val):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = life_val

    def bite(self, person):
        person.life_val -= self.attack_val
        print(f"{self.name}咬了{person.name}，{person.name}掉了{self.attack_val}点血, 还剩下{person.life_val}点血")


class Person:
    role = "person"

    def __init__(self, name, attack_val, life_val):
        self.name = name
        self.life_val = life_val
        # self.attack_val = attack_val
        self.weapon = Weapon() # 直接实例化

    def attack(self, dog):
        print(f"{self.name}打了{dog.name}，{dog.name}掉了{self.attack_val}点血")


class Weapon:

    def dog_stick(self, obj):
        '''打狗棒'''
        self.name = "打狗棒"
        self.attack_val = 40
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def knife(self, obj):
        '''刀'''
        self.name = "刀"
        self.attack_val = 50
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def gun(self, obj):
        '''枪'''
        self.name = "枪"
        self.attack_val = 100
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self, obj):
        print(f"{self.name}打{obj.name}，{obj.name}掉了{self.attack_val}点血, 还剩下{obj.life_val}点血")


d = Dog("旺财", "京巴", 30, 100)

p = Person("小明", 30, 100)
d.bite(p)
p.weapon.knife(d)