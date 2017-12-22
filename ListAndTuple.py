# -- coding: utf-8 --
print len([1,2,3]);
#数组合并
#+号用于组合列表，*号用于重复列表
print [1,2,3]+[4,5,6];
print ["Hi!"]*4;#['Hi!', 'Hi!', 'Hi!', 'Hi!']
print 3 in [1,2,3];#True
# 循环输出
for x in [1,2,3]:print  x;
# 循环截取
L=['panda','Panda','PANDA!'];
print L[2];#PANDA!
print L[-2];#Panda
print L[1:];#['Panda', 'PANDA!']
#  Python的元组与列表类似，不同之处在于元组的元素不能修改；
# 元组使用小括号()，列表使用方括号[]；元组创建很简单，只需要在括号中添加元素，并使用逗号(,)隔开即可
tup1=('physics','chemistry',1997,2000);
#元组中只有一个元素时，需要在元素后面添加逗号
tup1=(50,);
#元组中的元素值是不允许修改和删除的，可以使用del语句来删除整个元组
print tup1;
del tup1;
# 列表函数&方法
# list.append(obj) #在列表末尾添加新的对象
# list.count(obj) #统计某个元素在列表中出现的次数
# list.extend(seq) #在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)
# list.index(obj) #从列表中找出某个值第一个匹配项的索引位置，索引从0开始
# list.insert(index, obj) #将对象插入列表
# list.pop(obj=list[-1]) #移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值
# list.remove(obj) #移除列表中某个值的第一个匹配项
# list.reverse() #反向列表中元素，倒转
# list.sort([func]) #对原列表进行排序

# 元组内置函数
# cmp(tuple1, tuple2) 比较两个元组元素。
# len(tuple) 计算元组元素个数。
# max(tuple) 返回元组中元素最大值。
# min(tuple) 返回元组中元素最小值。
# tuple(seq) 将列表转换为元组。