# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：查找整数
@时间：2020/3/6  
"""

n = input()
arr = input().split()
s = input()
if s in arr:
    result = arr.index(s)
    print(result + 1)
else:
    print(-1)


