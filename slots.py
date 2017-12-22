# coding=utf-8
#__slots__()方法限制class属性--------------------------
class Student(object):
    # def __init__(self,name):
    #     self.name=name
    __slots__=('name','age')# 限制class的属性
    def set_age(self, age): # 定义一个函数作为实例方法
        self.age = age
s=Student()
s.name='bob'
s.set_age(12)
print s.age
# @property_________________把getter方法变成属性，只需加上@property就可以
class Student2(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 只定义getter方法，不定义setter方法就是一个只读属性
    @property
    def age(self):
        return 2014 - self._birth

print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3