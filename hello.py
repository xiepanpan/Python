#coding=utf-8
def hello():
    print("hello world")

def word():
    print("world")
# 切片--------------------------
L=range(10)
# 复制list
print L[:]
# 每隔两个取值
print L[::2]
# 前五个每隔三个取值
print L[:5:3]
# 取第四个到第七个数
print L[3:7]
# 迭代-------------------------------
from collections import Iterable
print(isinstance("abc",Iterable))

d={"1":"a","2":"b"}
for k,v in d.iteritems():
    print k,"=",v
# 列表生成式----------------------------
# 创建List 最外边是[]
# 创建generator生成器 最外边是()
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y
for x in "123":
    print x
print [x*x for x in range(1,11)]
print [x*x for x in range(1,11) if x%2==0]
print [m+n for m in "qwe" for n in "asd"]
# 生成器--------------------------
g=(x*x for x in range(10))
for x in g:
    print x
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print  b# print b 改为 yield 就会变为generator生成器
        a,b=b,a+b
        n=n+1
print fib(6)
# 高阶函数：把函数作为参数传入------------------
def add(x,y,f):
    return f(x)+f(y)
# abs是取绝对值
print add (-5,6,abs)

# map()作为高阶函数，可以传方法名和参数---------
def f(x):
    return x*x
print map(f,[1,2,3])
# 变为字符串型
print map(str,(1,2,3,4))
# reduce 函数结果应该是15，但现在结果是3，并报错--------------
from functools import reduce
def fn(x,y):
    print x*10+y
# print reduce(fn,[1,2,3,4,5])

def charm (s):
    return {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print map(charm,'123')
# filter()函数用于过滤序列---------------
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
# sorted 排序函数----------------------
print sorted([3,5,12,8])
# sorted 可作为高阶函数
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted((3,5,12,8),reversed_cmp)
print sorted(['bob', 'about', 'Zoo', 'Credit'])
# 不按大小写，之按字母顺序排序
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case)
# 返回函数,返回的是函数而不是数值，只有调用才会有值-----------------------------
# 求和
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f= lazy_sum(1,3,6,9)
print lazy_sum(1,3,6,9)()
# [1,2,3]
print range (1,4)
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1()

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print f1()
print f2()
print f3()

# 匿名函数：lambda------------------------
# 可以不写函数名

print map(lambda x:x*x,[1,2,3,4,5])

# 装饰器
def log(func):
    def wrapper(*args,**kw):
        print "call %s():"%func.__name__
        return func(*args,**kw)
    return wrapper

# @log相当于执行log(now)
@log
def now():
    print '2017-1-20'
print now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute log：')
def now():
    print '2013-12-25'
print now()

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