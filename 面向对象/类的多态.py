class Dog(object):
    def sound(self):
        print("汪汪汪....")


class Cat(object):
    def sound(self):
        print("喵喵喵....")


def make_sound(animal_type):
    """统一调用接口"""
    animal_type.sound()  # 不管传进来是什么动物，都调用sound方法


dogObj = Dog()
catObj = Cat()

make_sound(dogObj)
make_sound(catObj)
