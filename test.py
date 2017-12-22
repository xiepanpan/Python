#coding=utf-8
# import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

def now():
    print '2013-12-25'
print now()
# 偏函数-------------------------------------------
print int('100000',base=32)
import functools
int2=functools.partial(int,base=2)
print int2('1000')
# 相当于args = (10, 5, 6, 7)???????????????
# max(*args)
max2=functools.partial(max,10)
print max2(5,6,7)

import sys
def test():
    args=sys.argv
    if len(args)==1:
        print 'hell 1'
    else:
        print '22'
print test()

list1=[1,2,3]
print isinstance(list1,list)

print type(list1)









