class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("zhangsan", 18)

print(type(p))
print(type(Person))


def __init__(self, name, age):
    self.name = name
    self.age = age


dog_class = type("Dog", (), {"role": "dag", "__init__": __init__})

print(dog_class)
d = dog_class( "dalmation", 18)
print(d.role, d.name, d.age)
