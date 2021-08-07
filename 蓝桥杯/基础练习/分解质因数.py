# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：分解质因数
@时间：2020/3/21  
"""


# 判断质数
def isprime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


# 判断相乘质数条件是否满足
def satisfy(num2, c):
    for j in prime:
        if num2 % j == 0:
            satisfy_number[c] = str(j)
            num3 = int(num2 / j)
            if num3 > 1:
                if num3 in prime:
                    satisfy_number[c + 1] = str(num3)
                    break
                else:
                    satisfy(num3, c + 1)
                    break
            else:
                break


a, b = input().split()
prime = []
for i in range(2, int(b) + 1):
    if isprime(i):
        prime.append(i)

for i in range(int(a), int(b) + 1):
    satisfy_number = {}
    strline = '{}='
    satisfy(i, 0)
    for j in range(0, len(satisfy_number) - 1):
        strline = strline + satisfy_number[j] + "*"
    strline = strline + satisfy_number[len(satisfy_number) - 1]
    print(strline.format(i))
