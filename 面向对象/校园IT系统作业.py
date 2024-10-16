import datetime


class School(object):
    """学校类|总部"""

    def __init__(self, name, address, website):
        self.name = name
        self.address = address
        self.website = website
        self.balance = 0  # 账户余额
        self.branchSchool_list = [] # 分校列表
        self.class_list = [] # 班级列表
        print(f"创建了校区{name}, 地址是{address}")

    def count_stu_num(self):  # 统计学生人数
        pass

    def count_staff_num(self):  # 统计员工人数
        pass

    def staff_enrollment(self):  # 员工入职
        pass

    def count_total_revenue(self):  # 计算总收益
        print("-----校区总收入------")
        total_rev = self.balance
        print(self.name, self.balance)
        for b in self.branchSchool_list:
            print(b.name, b.balance)
            total_rev += b.balance

        print("各校区总收入：", total_rev)

    def count_class_list(self): # 统计班级列表
        print("-----各校区的班级列表------")
        print(self.name, self.class_list)
        for c in self.class_list:
            print(c.name, c.class_list)

    def __str__(self):
        return  self.name

    def __repr__(self):
        return self.name


class BranchSchool(School):
    """分校"""

    def __init__(self, name, address, website, parent_school_obj):
        super().__init__(name, address, website)
        self.parent_school_obj = parent_school_obj # 所属总部
        self.parent_school_obj.branchSchool_list.append(self)  # 将分校加入总部

class Course(object):
    """课程类"""

    def __init__(self, name, price, outline):
        self.name = name
        self.price = price
        self.outline = outline  # 课程大纲
        print(f"创建了课程{name},学费{price}")


class Class(object):
    """班级类"""

    def __init__(self, course_obj, semester, school_obj):
        self.course_obj = course_obj
        self.semester = semester
        self.school_obj = school_obj
        self.stu_list = []  # 学生列表
        school_obj.class_list.append(self) # 将自己加到校区的班级列表
        print(f"校区{school_obj.name}创建了班级{course_obj.name}-学期{semester}")

    def stu_transfer(self, stu_obj, new_class_obj):
        """将学生转班"""
        pass

    def __str__(self):
        return f"{self.school_obj.name}-{self.course_obj.name}-学期{self.semester}"
    def __repr__(self):
        return f"{self.school_obj.name}-{self.course_obj.name}-学期{self.semester}"

class Staff(object):
    """员工类"""

    def __init__(self, name, age, balance, salary, position, dept, school_obj):
        self.name = name
        self.age = age
        self.balance = balance
        self.salary = salary
        self.position = position
        self.dept = dept
        self.school_obj = school_obj

    def punch_card(self):
        """打卡"""
        pass


class Teacher(Staff):
    """老师类"""

    def __init__(self, name, age, balance, salary, position, dept, school_obj, course_obj):
        super().__init__(name, age, balance, salary, position, dept, school_obj)
        self.course_obj = course_obj

    def teach_class(self, class_obj, day):
        print(f"老师{self.name}在{day}讲了{class_obj}")


class Student(object):
    """学生类"""

    def __init__(self, name, age, balance, class_obj):
        self.name = name
        self.age = age
        self.balance = balance
        self.class_obj = class_obj

        # 加入班级
        class_obj.stu_list.append(self)
        # 交学费
        class_obj.school_obj.balance += class_obj.course_obj.price
        self.balance -= class_obj.course_obj.price
        print(f"学生{name}注册了，班级是{class_obj}, 交了学费{class_obj.course_obj.price}元")

    def punch_card(self):
        print(f"{datetime.datetime.now()}:学生{self.name}在{self.class_obj}上课")


# 创建校区
headquarters = School("IT教育集团", "深圳南山", "www.itcast.cn")
sha1n_school = BranchSchool("深圳分校", "深圳宝安", "www.itcast.cn", headquarters)
sha2n_school = BranchSchool("上海分校", "上海徐汇", "www.itcast.cn", headquarters)
sha3n_school = BranchSchool("广州分校", "广州天河", "www.itcast.cn", headquarters)
# 创建课程
py_course = Course("Python全栈", 5000, "Python基础、Python进阶、Python项目")
linux_course = Course("Linux运维", 3000, "Linux基础、Linux系统管理、Linux系统优化")
test_course = Course("软件测试", 4000, "软件测试基础、Web测试、移动测试")
go_course = Course("Go语言", 5000, "Go语言基础、Go语言进阶、Go语言项目")

# 创建班级
py_24 = Class(py_course, "24期", headquarters)
py_12 = Class(py_course, "12期", sha1n_school)
linux_24 = Class(linux_course, "24期", sha2n_school)
test_24 = Class(test_course, "24期", sha3n_school)
go_23 = Class(go_course, "23期", headquarters)

# 创建员工、老师、学生

s1 = Staff("Alex", 26, 0, 4000, "CEO", "总经办", headquarters)
s2 = Staff("Bob", 28, 0, 30000, "CTO", "总经办", sha1n_school)
s3 = Staff("Cindy", 26, 0, 20000, "HR", "HR", sha2n_school)

t1 = Teacher("Tom", 26, 0, 5000, "讲师", "教学部", headquarters, py_course)
t2 = Teacher("Jerry", 28, 0, 5000, "讲师", "教学部", sha1n_school, linux_24)
t3 = Teacher("Mary", 26, 0, 5000, "讲师", "教学部", sha2n_school, go_course)
t4 = Teacher("Lucy", 26, 0, 5000, "讲师", "教学部", sha3n_school, test_course)

s1 = Student("小明", 18, 15000, py_24)
s2 = Student("小红", 19, 15000, py_12)
s3 = Student("小刚", 20, 15000, linux_24)
s4 = Student("小花", 21, 15000, test_24)
s5 = Student("小王", 22, 15000, go_23)

headquarters.count_total_revenue()
headquarters.count_class_list()
