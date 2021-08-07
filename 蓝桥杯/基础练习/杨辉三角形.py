# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：杨辉三角形
@时间：2020/3/6  
"""

b = [[1],[1,1]]
n = int(input())
if n == 1:
    print(1)
else:
    for i in range(2,n):
        c =[]
        c.insert(0,1)
        for j in range(1,i):
            c.insert(j,b[i-1][j-1]+b[i-1][j])#核心
        c.append(1)
        b.insert(i,c)
for out in b:
    for i in out:
        print(i,end=" ")
    print()



