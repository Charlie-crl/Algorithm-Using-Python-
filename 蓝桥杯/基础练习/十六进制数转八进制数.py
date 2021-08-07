# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：十六进制数转八进制数
@时间：2020/3/7  
"""

m = []
n = int(input())
for i in range(n):
    m.append(input())
for i in m:
    print("%o"%int(i,16))

