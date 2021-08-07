# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：星星右顶向三角形
@时间：2020/3/11  
"""
"""
i = 1
while i <= 9:
    j = 1
    if i <= 5:
        p = i
    else:
        p = 10 - i
    while j <= p:
        print("*", end="")
        j += 1
    print("")
    i += 1
"""

"""
i = 1
while i<=9:
    if i <=5:
       print("*"*i)
    else:
        print("*"*(10-i))
    i = i+1
"""


i = 9
j = 8
while i>0:
    k =j
    while k<i:
        print('*',end='')
        k = k+1
    print()
    i=i-1
    if not j == 0:
        j = j-2

