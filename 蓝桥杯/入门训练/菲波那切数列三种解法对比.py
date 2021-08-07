# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：菲波那切数列三种解法对比
@时间：2020/3/11  
"""

import time
start = time.perf_counter()
#循环不变量，速度最快
# N = 30
# a=1
# b=1
# c=1
# for i in range(2,N):
#    c = b+a
#    a = b
#    b = c
# print(c)

#递归
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1) + f(n-2)
# print(f(30))

#尾递归：
#递归调用是整个函数体中最后执行的语句且它的 返回值不属于表达式的一部分。
#特点：回归过程中不用做任何操作，这个特性很重要，因 为大多数现代编译器会利用这种特点自动生成优化的代码。

def f(n,a,b):
    if n == 0:
        return a
    else:
        return f(n-1,b,a+b)
print(f(30,0,1))

end = time.perf_counter()
print(end-start)

