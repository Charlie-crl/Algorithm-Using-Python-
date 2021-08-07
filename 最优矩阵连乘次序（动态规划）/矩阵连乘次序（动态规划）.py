# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：矩阵连乘次序（动态递归）
@时间：2020/4/13
"""
import copy

# 数据准备
# 矩阵的行列数
p = [30, 35, 15, 5, 10, 20, 25]
# n矩阵个数
n = len(p) - 1
m = {}
for i in range(1, n + 1):
    m[i] = {}
for key, value in m.items():
    value[key] = 0
s = copy.deepcopy(m)


# 主体算法
def matrix_multi():
    # r:矩阵连乘的个数
    for r in range(2, n + 1):
        # i最左端位置
        for i in range(1, n - r + 1 + 1):
            # j最右端位置
            j = i + r - 1
            # 递推式
            m[i][j] = 0 + m[i + 1][j] + p[i - 1] * p[i] * p[j]
            # 次序分割位置，i为初始分割位置
            s[i][j] = i
            # 寻找多种可能结果（计算次数比较），求min,k为分割位置
            for k in range(i + 1, j):
                t = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if t < m[i][j]:
                    m[i][j] = t
                    s[i][j] = k


# 输出最优解
def better_result(i, j):
    if i == j:
        return
    better_result(i, s[i][j])
    better_result(s[i][j] + 1, j)
    print("矩阵A{}--矩阵A{}".format(i, s[i][j]))
    print("矩阵A{}--矩阵A{}".format(s[i][j] + 1, j))


# 程序入口
matrix_multi()
better_result(1, n)
print("最少计算次数为%d" % m[1][n])
