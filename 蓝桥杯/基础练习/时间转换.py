# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：时间转换
@时间：2020/3/7  
"""

n = int(input())
hours = n // 3600
h = n % 3600
minutes = h // 60
s = h % 60
print("{}:{}:{}".format(hours,minutes,s))


