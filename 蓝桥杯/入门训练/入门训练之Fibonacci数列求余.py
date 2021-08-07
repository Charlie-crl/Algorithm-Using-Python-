# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：菲波那切数列的数求余
@时间：2020/3/3  
"""
# import time
# start = time.perf_counter()
N = int(input())
# N = 10
a=1
b=1
c=1
for i in range(2,N):
   c = (b+a) % 10007
   a = b
   b = c
print(c)



# end = time.perf_counter()
# print(end-start)