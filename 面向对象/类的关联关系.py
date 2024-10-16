class Relationship:
    """保存couple之间的对象关系"""

    def __init__(self, ):
        self.couple = []

    def make_couple(self, p1, p2):
        self.couple = [p1, p2]
        print("{} and {} are couple".format(p1.name, p2.name))

    def het_my_parter(self, p):
        for couple in self.couple:
            if couple != p:
                return couple
        else:
            print("{} don't have parter".format(p))

    def break_couple(self):
        print("{} and {} break couple".format(self.couple[0].name, self.couple[1].name))
        self.couple.clear()

class Person:
    def __init__(self, name, age, sex, relationship):
        self.name = name
        self.age = age
        self.sex = sex
        self.relationship = relationship # 关联关系 每个人的实例存储
        # self.parter = None  # 应该是一个对象， 代表另一半

    def do_private_stuff(self):
        print("doing private stuff")
        pass


r = Relationship()
p1 = Person("zhangsan", 18, "male", r)
p2 = Person("lisi", 19, "female", r)
r.make_couple(p1, p2)
# 双休关联
# p1.parter = p2
# p2.parter = p1

print(p1.relationship.couple, p2.relationship.couple)
# 取消关联
# p2.parter = None
# p1.parter = None

print(p1.relationship.het_my_parter(p1).name)
