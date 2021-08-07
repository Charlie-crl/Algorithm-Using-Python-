# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：水仙花数
@时间：2020/3/6  
"""

for i in range(100,1000):
    if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == i:
        print(i)

