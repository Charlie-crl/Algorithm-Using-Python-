# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：分支限界（FIFO）算法
@时间：2020/6/9  
"""

# 初始化
W = input("请输入所有集装箱的重量，以空格隔开\n").split()
w = list(map(int, W))
w.insert(0, 0)
c1, c2 = input("请分别输入船1和船2的载重量，以空格隔开\n").split()
n = len(w) - 1  # 集装箱数量
cw = 0  # 当前船1装载量
i = 1  # 当前层数
r = sum(w)  # 剩余集装箱重量
best_w = 0  # 当前最优装载量
stack = [-1]    # 记录栈，-1为分层标志
r = r - w[1]
while len(stack) != 0: # 分支限界算法
    if cw + w[i] <= int(c1):    # 不超过船一的重量
        if cw + w[i] > best_w:  # 寻找最优值
            best_w = cw + w[i]
        if i < n:
            stack.append(cw + w[i])   # 可扩展节点入队
    if cw + r > best_w and i < n:   # 限界函数，不可能超过bestw的分支剪掉
        stack.append(cw)
    cw = stack.pop(0)   # 死结点出队
    if cw == -1:
        if len(stack) == 0:
            break
        stack.append(-1)
        cw = stack.pop(0)
        i = i + 1
        r = r - w[i]
print(best_w)
