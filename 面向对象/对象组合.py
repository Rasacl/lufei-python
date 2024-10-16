class Dog:
    role = "dog"

    def __init__(self, name, breed, attack_val):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val

    def bite(self, person):
        person.life_val -= self.attack_val
        print(f"{self.name}咬了{person.name}，{person.name}掉了{self.attack_val}点血, 还剩下{person.life_val}点血")


class Person:
    role = "person"

    def __init__(self, name, attack_val, life_val):
        self.name = name
        self.life_val = life_val
        self.attack_val = attack_val

    def attack(self, dog):
        print(f"{self.name}打了{dog.name}，{dog.name}掉了{self.attack_val}点血")


d1 = Dog("旺财", "秋田犬", 10)
p1 = Person("小明", 5, 100)
p1.attack(d1)
d1.bite(p1)