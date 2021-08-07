# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：字符串对比
@时间：2020/3/7  
"""

str1 = input()
str2 = input()
if not len(str1) == len(str2):
    print(1)
elif str1 == str2:
    print(2)
elif str1.upper() == str2.upper():
    print(3)
else:
    print(4)