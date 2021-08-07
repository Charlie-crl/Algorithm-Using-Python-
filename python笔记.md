# python偏方
### eval：
eval除了可以计算字符串里的表达式，还可以起到去字符串化(一层)的作用 
类似于int（）,但int只能用于`‘整数’`，eval还可以用于`‘浮点数’`的去字符化

### 数字的四舍五入：
**妙法：** 
**使用 int()** 将小数转换为整数，小数取整会采用比较暴力的截断方式，即向下取整。
（注：5.5向上取整为6，向下取整为5） 
正常情况下 int(5.5) 结果为5 
如果想要让其按照**人类的思维**“四舍五入”:

> 5.4 “四舍五入”结果为：5，int(5.4+0.5) == 5 
> 5.6 “四舍五入”结果为：6，int(5.6+0.5) == 6

**当我们需要对整数 或者 浮点数进行四舍五入的时候。** 
round(value, ndigits) /// 内置函数 
对浮点数进行四舍五入(传入的ndigit应该是正值，作用于十分位、百分位...)：

```python
print( round(1.23, 1) ) # 1.2
print( round(1.27, 1) ) # 1.3  
print( round(-1.27, 1) ) #-1.3  
print( round(1.25361, 3)) #1.254  
print( round(2.5, 0) ) #2.0
```
*当整数位为偶数时，如2.5=>2.0,2.55=>3.0,因为2.5在机器里为2.446。。。* 
对整数进行四舍五入(传入的ndigit应该是自然数，作用于个位、十位、百位...)

```python
print( round(314159, -1)) #314160
print( round(314159, -2)) #314200  
print( round(314159, -3)) #314000
```
### format格式化

![img](https://img-blog.csdn.net/20180626143328893?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjI4MDUxNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

```python
pi = 3.1415926
x = 1234.56789
print( format(pi, '0.2f')) #3.14
print( format(pi, '0.3f')) #3.142
print( 'the value is {:0.4f}'.format(pi) ) #the value is 3.1416
print(format(x, '>10.1f'))   #'    1234.6'
print(format(x, '<10.10f'))  #'1234.5678900000'
print(format(x, '^10.1f'))   #'  1234.6  '
print(format(x, ','))        #1,234.56789
print(format(x, 'e'))        #1.234568e+03科学计数法
print('The value is {:0,.2f}'.format(x)) # The value is 1,234.57
print(f'The value is {x:0,.2f}') # The value is 1,234.57
```
### 复制
如d=a为浅复制，直接复制引用。 
`d=a[:]`或import copy ,d=copy.deepcopy(a)为深复制 
或d = a.copy()

### 进制转换
**其他进制转十进制：** 
`int(a,base=2 or 8 or 16 )` 
**转二进制** 
`bin()` 
**转八进制** 
`oct()` 
**转16进制** 
`hex()` 
若要输出0X： 
`print("%X"%a)` 
*pass:oct(),bin(),hex()输出类型均为字符串*

### for循环获得遍历下标：
如`for index,i in enumerate(arr):`

### for-else用法

```py
# eg1
import numpy as np
for i in np.arange(5):
    print i
else:
    print("hello？")
# 0
# 1
# 2
# 3
# 4
# hello？

```

```py
# eg2
import numpy as np
for i in np.arange(5):
    print i
    if (i == 3):
        break
else:
    print("hello？")
# 0
# 1
# 2
# 3

```

> 可以发现，else当且仅当for中的break没有执行时，执行

##### 应用场景

```py
# 求一百内的素数之和
sum=0
for n in range(2,100):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        sum+=n
print(sum)
```



### 列表推导式——轻量级循环

列表推导式（list
comprehension）是利用其他列表创建新列表的一种方法。它的工作方式类似于for循环。

    [x*x for x in range(10)]  
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
列表由range(10)中每个x的平方组成。太容易了？如果只想打印出那些能被3整除的平方数呢？ 
那么可以使用模除运算符——y%3，当数字可以被3整除时返回0 
（注意，x能被3整除时，x的平方必然也可以被3整除）。 
这个语句可以通过增加一个if部分添加到列表推导式中:

    [x*x for x in range(10) if x % 3 == 0] [0, 9, 36, 81]
也可以增加更多for语句的部分：

    [(x, y) for x in range(3) for y in range(3)]
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
　　作为对比，下面的代码使用了两个for语句创建了相同的列表：
 ```python
 result = [] 
 for x in range(3):
 for y in range(3): 
    result.append((x, y))
 print(result)
 ```
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

　　也可以和if子句联合使用：
```python
girls = ['alice', 'bernice', 'clarice'] 
boys =['chris', 'arnold', 'bob'] 
[b+'+'+g for b in boys for g in girls if b[0]== g[0]] 
```
    ['chris+clarice', 'arnold+alice', 'bob+bernice'] 

　　这样就得到了那些名字首字母相同的男孩和女孩。

　　更优方案

　　男孩/女孩名字对的例子其实效率不高，因为它会检查每个可能的配对。
```python
 girls = ['alice', 'bernice', 'clarice']
 boys = ['chris', 'arnold', 'bob']
 letterGirls = {}
 for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
    print[b+'+'+g for b in boys for g in letterGirls[b[0]]]
```
    ['chris+clarice', 'arnold+alice', 'bob+bernice']

　　这个程序建造了一个叫做letterGirl的字典，其中每一项都把单字母作为键， 以女孩名字组成的列表作为值。在字典建立之后，列表推导式循环整个男孩集合， 并且查找那些和当前男孩名字首字母相同的女孩集合。 这样列表推导式就不用尝试所有的男孩女孩的组合，检查首字母是否匹配。

### 面向对象Tips：

1.为方便维护代码，一般一个**角色**（如学员管理系统中的*学员类*和*管理系统类*）一个程序文件（py）

2.系统要有主程序入口，一般为main.py

### pycharm问题：

基于pycharm导入模块显示不存在的解决方法：

**解决办法：**pycharm不会将当前文件目录自动加入自己的sourse_path。右键make_directory as-->sources path将当前工作的文件夹加入source_path就可以了。

### Python chr() 函数：

```
print chr(0x30), chr(0x31), chr(0x61)   # 十六进制
0 1 a
print chr(48), chr(49), chr(97)         # 十进制
0 1 a
```

**特例**：chr（12288）表示中文空格的编码

在print一组数据，每一行中英文混行，需要对齐时，可在输出中文的那一列进行format控制

如下，打印中国高校排名

```
tplt = "{0:^10}\t{1:^10}\t{2:^10}"
    print(tplt.format("学校名称", "位置", "分数"))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2]))
```

把字符串宽度都定义为10，但是中文本身的宽度都不到10所以会填充西文空格，就会导致字符的实际宽度长短不一

![img](https://img2018.cnblogs.com/blog/1494421/201810/1494421-20181010162847347-4165194.png)

解决方法：宽度不够时采用中文空格填充

中文空格的编码为chr(12288)

 

```
tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("学校名称", "位置", "分数", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
```

![img](https://img2018.cnblogs.com/blog/1494421/201810/1494421-20181010163538763-1944987724.png)



### 全局与局部变量问题：

​	全局与局部判断的参照物是函数，所以类似for循环里定义的变量为全局变量

### 关于（+=与=+）问题

如：

```py
def jia(a):
    a += a
    print(a)
aa = [1]
jia(aa)
print(aa)
```

结果：

	[1, 1]
	[1, 1]

而

```py
def jia(a):
    a = a + a
    print(a)
aa = [1]
jia(aa)
print(aa)
```

结果：

```
[1, 1]
[1]
```

因为：
	![](C:\Users\陈先生\Desktop\Camera Roll\捕获.PNG)

### 函数

![](C:\Users\陈先生\Desktop\Camera Roll\捕获1.PNG)

### Python中进行None判断时，为什么用is而不是==

「is和None区别在哪里」
is比较的是对象标识符，用来检查对象的标识符是否一致，即两个对象在内存中的地址是否一致。在使用a is b的时候，相当于是做id(a)==id(b)判断。
==比较两个对象的值是否相等，相当于调用__eq__()方法，即a==b等同于a.__eq__(b)。
「进行None判断时，为什么用is」
▍这在PEP8中有所规定
“Comparisons to singletons like None should always be done with ‘is’ or ‘is not’, never the equality operators.”
— From PEP8

▍为什么会有这样的规定
如上所述None在Python里是个单例对象，一个变量如果是None，它一定和None指向同一个内存地址。None是python中的一个特殊的常量，表示一个空的对象。空值是Python中的一个特殊值，数据为空并不代表是空对象，例如[]，''，()，{}等都不是None。

a = None
b = None
print(id(a) == id(b)) # True

print([] is None) # False
print('' is None) # False
1
2
3
4
5
6
None和任何对象比较返回值都是False，除了自己。==None背后调用的__eq__()，而__eq__()可以被重载，e.g.

class test():
    def __eq__(self, other):
        return True

t = test()
print(t is None) # False
print(t == None) # True
1
2
3
4
5
6
7
虽然很多时候用==None会得到我们内心想要的结果，但是如果一个对象的__eq__()方法被重载，==操作可能会影响结果的判断。对了，像PyCharm这样的IDE一般会提示==None不符合PEP8规范，不知大家注意过没有。

另外从代码执行效率上来看，is is a LOT faster than ==。

