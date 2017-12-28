# -- coding: utf-8 --

# 访问字典里的值
dict ={'name':'Zara','age':22,'class':'First'};
print "字典dic的name值为",dict['name'];
print "dic['age']:",dict['age'];

# 修改字典
dict["age"]=27;
dict["school"]="sdau";
print "dict['age']:",dict['age'];
print "dict['school']:",dict['school'];

# 删除字典
del dict['name'];
dict.clear();
del dict;

# cmp(dict1, dict2) #比较两个字典元素。
# len(dict) #计算字典元素个数，即键的总数。
# str(dict) #输出字典可打印的字符串表示。
# type(variable) #返回输入的变量类型，如果变量是字典就返回字典类型。
# clear() #删除字典内所有元素
# copy() #返回一个字典的浅复制
# fromkeys() #创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# get(key, default=None) #返回指定键的值，如果值不在字典中返回default值
# has_key(key) #如果键在字典dict里返回true，否则返回false
# items() #以列表返回可遍历的(键, 值) 元组数组
# keys() #以列表返回一个字典所有的键
# setdefault(key, default=None) #和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# update(dict2) #把字典dict2的键/值对更新到dict里
# values() #以列表返回字典中的所有值
import time,datetime;
localtime=time.localtime(time.time());
print "local current time",localtime;

# 字符串转换为日期
expire_time="2017-12-28 09:50:35";
d=datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S");
print d;

# 获取日期差
oneday=datetime.timedelta(days=1);
today=datetime.date.today();
yesterday=datetime.date.today()-oneday;
tomorrow=datetime.date.today()+oneday;
today_zero_time=datetime.datetime.strftime(today,'%Y-%m-%d %H:%M:%S');
print datetime.timedelta(milliseconds=1);
print datetime.timedelta(seconds=1);
print datetime.timedelta(minutes=1);
print datetime.timedelta(hours=1);
print datetime.timedelta(days=1);
print datetime.timedelta(weeks=1);

# 获取时间差
today_time=datetime.datetime.now();
yesterday_time=datetime.datetime.now()-oneday;
tomorrow_time=datetime.datetime.now()+oneday;
print datetime.datetime.strftime(today_time,'%Y-%m-%d %H:%M:%S');
print datetime.datetime.strftime(yesterday_time,'%Y-%m-%d %H:%M:%S');
print datetime.datetime.strftime(tomorrow_time,'%Y-%m-%d %H:%M:%S');

# 字符串日期格式化为秒数
d=datetime.datetime.strptime(expire_time,'%Y-%m-%d %H:%M:%S')
time_sec_float=time.mktime(d.timetuple());
print time_sec_float;
# 日期格式化为秒数
d=datetime.date.today()
time_sec_float=time.mktime(d.timetuple())
print time_sec_float;
# 秒数转字符串
time_sec=time.time()
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time_sec));

