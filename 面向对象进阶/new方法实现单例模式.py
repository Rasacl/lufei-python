class Student(object):
    def __init__(self, name):
        self.name = name
        print('init hhhh')

    def __new__(cls, *args, **kwargs):
        # 负责执行__init__
        print(cls, args, kwargs)

        return object.__new__(cls) 
