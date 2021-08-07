# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：回文数
@时间：2020/3/6  
"""

def if_stack(number):
    stack = []
    result = ''
    number2 = list(number)
    for i in number2:
        stack.append(i)
    for i in range(4):
        result = result +stack.pop()
    if result == number:
        return True
    else:
        return False
for i in range(1000,10000):
    if if_stack(str(i)):
        print(i)