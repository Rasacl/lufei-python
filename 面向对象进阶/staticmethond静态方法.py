# 静态方法 不能访问实例变量和类变量 静态方法隔离了他跟类和实例的关系

class Student(object):
    role = "student"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def fly(self):
        print(self.name, "is flying....")


s = Student("xiaoming")
s.fly()
