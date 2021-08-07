# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：特殊回文数
@时间：2020/3/6  
"""

# def if_stack(number):
#     stack = []
#     result = ''
#     number2 = list(number)
#     for i in number2:
#         stack.append(i)
#     for i in range(len(number)):
#         result = result +stack.pop()
#     if result == number:
#         return True
#     else:
#         return False
# n = int(input())
# for i in range(10000,1000000):
#     if i < 100000:
#         if int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + \
#                 int(str(i)[3]) + int(str(i)[4]) == n:
#             if if_stack(str(i)):
#                 print(i)
#     else:
#         if  int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + \
#                 int(str(i)[3]) + int(str(i)[4]) + int(str(i)[5]) == n:
#             if if_stack(str(i)):
#                 print(i)

#人为构造回文数，不用再判断
n = int(input())
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            if 2*i+2*j+k == n:
                print("{0}{1}{2}{3}{4}".format(i,j,k,j,i))
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            if 2*i+2*j+2*k == n:
                print("{0}{1}{2}{3}{4}{5}".format(i,j,k,k,j,i))
