# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：入门训练之A+B问题
@时间：2020/3/4  
"""


# number = input().split(" ")
# a, b = number
# print(int(a)+int(b))

#eval函数可直接运算内含表达式的字符串
n = input()
print(eval(n.replace(" ", "+")))