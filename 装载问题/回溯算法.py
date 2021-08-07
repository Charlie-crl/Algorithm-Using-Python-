# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：回溯算法
@时间：2020/6/7  
"""

# 初始化
W = input("请输入所有集装箱的重量，以空格隔开\n").split()
w = list(map(int, W))
w.insert(0, 0)
c1, c2 = input("请分别输入船1和船2的载重量，以空格隔开\n").split()
all_x = []  # 所有装载方案
n = len(w) - 1  # 集装箱数量
x = n*[0] + [0]  # 当前集装箱装载方案，1表示装载，0反之
cw = 0  # 当前船1装载量
item = 1  # 当前层数
r = sum(w)  # 剩余集装箱重量
right = []  # 记录可行解


# 回溯
def backtrack(i):
    global r, cw
    if i > n:  # 到达叶子节点
        y = x.copy()
        all_x.append(y)  # 记录解
        return
    r = r - w[i]
    if cw + w[i] <= int(c1):  # 搜索左子树
        x[i] = 1
        cw = cw + w[i]
        backtrack(i + 1)
        cw = cw - w[i]
    # 搜索右子树
    x[i] = 0
    backtrack(i + 1)
    r = r + w[i]


# 执行
backtrack(item)

# 筛选可行解
for j in all_x:
    _sum = 0
    for wi, xi in list(zip(w, j)):
        _sum = _sum + wi * (1 - xi)  # _sum:装载船1后的剩余集装箱重量
    if _sum <= int(c2):   # 装载c1后剩余的重量是否<=c2?
        right.append(j)

# 输出
print("所有可行解为：")
for a in right:
    for wj, xj in list(zip(w, a)):
        if xj == 1:
            print(wj, end=',')
    print()
