class Dog:
    def __init__(self, name, age, breed, master):
        self.name = name
        self.age = age
        self.breed = breed
        self.master = master
        self.say_hello()

    def say_hello(self):
        print(f"我的主人是{self.master.name}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk_dog(self, dog):
        print(f"{self.name}正在和{dog.name}玩")


person = Person("小明", 18)
dog = Dog("旺财", 3, "秋田犬", person)
person.walk_dog(dog)
