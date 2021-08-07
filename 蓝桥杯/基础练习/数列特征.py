# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：数列特征
@时间：2020/3/5  
"""
brr =[]
number = int(input())
arr = input().split()
for index,i in enumerate(arr):#去字符化
    brr.insert(index,int(i))
print(max(brr))
print(min(brr))
print(sum(brr))
