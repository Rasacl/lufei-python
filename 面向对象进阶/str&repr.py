class Person(object):
    def __init__(self, name, addr, type):
        self.name = name
        self.addr = addr
        self.type = type

    def __str__(self):
        return "str---》name: %s, addr: %s, type: %s" % (self.name, self.addr, self.type)
    def __repr__(self):
        return "repr---》name: %s, addr: %s, type: %s" % (self.name, self.addr, self.type)

p = Person("zhangsan", "beijing", "student")
print(str(p))
print(repr(p))
print(p)