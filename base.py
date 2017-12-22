# var1=11;
# print var1;
print("hello")
str='''ge'''
print (str)
str1='he"dd"'
print (str1)


import  re
text="oo on sss"
m=re.match('oo',text)
if m :
   print(m.group())
else:
    print(None)


# 换行
print('''l1
l2''')

# 与and    或or   非not
flage=not True
print (flage)

a='ab'
b=a
a='ss'
print(b)

# 输出ASCII码和对应数字
print(ord('a'),chr(65))


# 格式化字符串 %d 整数 %s字符串 %f 浮点数
print('hello,%s' % 'world')
print('hi,%s you have $%d' %('aa',100))
print('%.2f'%3.1415926)

print('growth rate : %d %%'% 7)
# Unicode
print(u'中文')


# 数组
alist=['a','b']
# 追加到最后
alist.append('c')
print(alist)
# 插入到指定位置
alist.insert(1,'d')
print(alist)
# 删除末尾元素  pop()
alist.pop()
print(alist)
# 删除指定位置元素 pop(i)
alist.pop(0)
print(alist)
# 把某个元素替换成别的元素
alist[0]='a'
print(alist)
L=['a','b']
La=['A','B',L,'C']
print(La)


# tuple 不可变数组
t=(1,2)
print(t)


# 判断
age=3
if age>18:
    print ('adult')
elif age>6 :
    print('teenager')
else:
    print('kid')

# 非零数值、非空字符串、非空list
a=0
if a:
    print('true')
else:
    print('false')

# for循环
sum=0
for x in [1,2,3,4,5]:
    sum=sum+x
print(sum)
# range(5) --是从0开始小于5的整数
sum=0
for x in range(5):
    sum = sum + x
print(sum)

sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)

# dict key-value   dict的key必须是不可变对象
d={'aa':98,'bb':95}
print(d['bb'])
# 添加dict元素
d['cc']=66
print(d['cc'])

print('dd'in d)
# 通过dict提供的get方法，如果key不存在，可以返回None
print(d.get('dd',None))

print(3 in {1,2,3}^{3,4,5})

# list[] 列表 tuple()元组  dict{key:value}字典 set{}集合
# tuple[1]=4 不能赋值tuple的单个元素的值，但是可以一次性覆盖tuple所有元素的值
list1=[1,2,3]
tuple=(1,2,3)
print(list1[1])
print(tuple[1])
# 所有类型本身的类型是TypeType-------------------------
# 判断变量时候是某个类型用isinstance()
print isinstance(list1,list)
# 基本类型可以用type()判断
print type(list1)








