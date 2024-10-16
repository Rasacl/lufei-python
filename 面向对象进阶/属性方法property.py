# 属性方法 property 把方法变成属性调用

class Student(object):
    role = "student"

    def __init__(self, name):
        self.name = name

    @property
    def fly(self):
        print(self.name, "is flying....")


s = Student("xiaoming")
s.fly