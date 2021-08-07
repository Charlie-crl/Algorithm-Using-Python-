# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：数列排序
@时间：2020/3/7  
"""

n = int(input())
m = input().split()
l = [int(x) for x in m]
l.sort()
for i in l:
    print(i,end=' ')

