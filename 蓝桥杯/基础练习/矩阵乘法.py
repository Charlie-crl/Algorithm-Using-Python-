# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：矩阵乘法
@时间：2020/3/22  
"""

# n = 阶数， m = 幂数
n, m = input().split()
# 将输入的矩阵写入
start = []
for i in range(int(n)):
    start.append(input().split())


# print(start)

# 生成“竖排列表”
def vertical(e):
    o = []
    for j in range(int(n)):
        l = []
        for k in e:
            l.append(k[j])
        o.append(l)
    return o


# print(vertical(start))
# 矩阵乘法
def matrix_multi(x, y):
    q = []
    for i in x:
        p = []
        for j in y:
            a = 0
            for u in range(int(n)):
                a = a + int(i[u]) * int(j[u])
            p.append(a)
        q.append(p)
    return q


# 自定义输出
def _print(end_list):
    for iii in end_list:
        for jjj in iii:
            print(int(jjj), end=' ')
        print()


# 幂运算，递归形式
def mi(xx, num):
    q2 = matrix_multi(xx, o2)
    if num == 2:
        _print(q2)
    else:
        mi(q2, num - 1)


# 程序的开始
if m == '0':
    EE = []
    for ii in range(int(n)):
        E = []
        for jj in range(int(n)):
            if not jj == ii:
                E.insert(jj, 0)
            else:
                E.insert(jj, 1)
        EE.append(E)
    _print(EE)
elif m == '1':
    _print(start)
else:
    o2 = vertical(start)
    mi(start, int(m))
