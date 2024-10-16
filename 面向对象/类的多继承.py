# python 2 经典类深度优先 新式类是广度优先
# python 3 都是广度优先
class Base(object):  # 新式类
    def fight(self):
        print("动物会打")


class shenxianBase(Base):
    def fight(self):
        print("神仙始祖在天地边界打架")


class shenxian(shenxianBase):
    def fly(self):
        print("神仙都会飞")

    def fight(self):
        print("神仙都会打")


class MonkeyBase(Base):
    def fight(self):
        print("猿猴都会打")


class Monkey(MonkeyBase):
    def eat_peach(self):
        print("猴子都喜欢吃桃子")

    def fight(self):
        print("猴子都会打")


class MonkeyKing(shenxian, Monkey):
    def paly_goden_stick(self):
        print("孙悟空喜欢金箍棒")


m = MonkeyKing()
m.fly()
m.eat_peach()
m.paly_goden_stick()

m.fight()
