# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：多处理机调度问题
@时间：2020/4/27  
"""

"""
问题描述：
7个独立作业{1,2,3,4,5,6,7}由3台机器M1，M2和M3加工处理。
各作业所需的处理时间分别为{2,14,4,16,6,5,3}
贪心算法实现，最长时间作业优先优先
用到：优先队列：二叉堆
"""


# 构造自己需要的二叉堆
class BinaryHeap:
    def __init__(self):
        """用1,2,3下标位来分别表示M1，M2，M3，先初始化为0，开头0位占位"""
        self.heap_list = [0, 0, 0, 0]

    def insert(self, i):
        """二叉堆的插入新数据"""
        self.heap_list.append(i)
        self.move_up()

    def move_up(self):
        """插入后的上移"""
        if self.heap_list[3] < self.heap_list[1]:
            tmp = self.heap_list[1]
            self.heap_list[1] = self.heap_list[3]
            self.heap_list[3] = tmp

    def del_min(self):
        """弹出最小值"""
        _min = self.heap_list[1]
        self.heap_list[1] = self.heap_list[3]
        self.heap_list.pop()
        self.move_down()
        return _min

    def move_down(self):
        """弹出后的下移"""
        if self.heap_list[2] < self.heap_list[1]:
            tmp = self.heap_list[1]
            self.heap_list[1] = self.heap_list[2]
            self.heap_list[2] = tmp






# 数据准备
my_binary_heap = BinaryHeap()
M1 = []
M2 = []
M3 = []
m1 = 0
m2 = 0
m3 = 0
sum_task = 0
tasks = {
    # time:work
    2: 1,
    14: 2,
    4: 3,
    16: 4,
    6: 5,
    5: 6,
    3: 7
}
times = [2, 14, 4, 16, 6, 5, 3]
times.sort()






# 程序入口
while len(times):
    # 最长时间作业优先出栈
    new_task = times.pop()
    # 弹出的最小值
    old_task = my_binary_heap.del_min()
    # 帮三台机器分配作业
    if old_task != 0:
        if old_task == m1:
            M1.append(new_task)
            sum_task = old_task + new_task
            m1 = sum_task
        elif old_task == m2:
            M2.append(new_task)
            sum_task = old_task + new_task
            m2 = sum_task
        elif old_task == m3:
            M3.append(new_task)
            sum_task = old_task + new_task
            m3 = sum_task
        else:
            pass
    else:
        sum_task = new_task
    my_binary_heap.insert(sum_task)
    # 三台机器初始化
    if len(M1) == 0:
        M1.append(new_task)
        m1 = new_task
    elif len(M2) == 0:
        M2.append(new_task)
        m2 = new_task
    elif len(M3) == 0:
        M3.append(new_task)
        m3 = new_task
    else:
        pass

# 构造输出
print("每台机器完成的时间：")
M = [M1, M2, M3]
for num, i in enumerate(M):
    print("机器{}：{}".format(num + 1, sum(i)))
    print("分别是：")
    for f in i:
        print(f, end=',')
    print()
print("总时间为:", max(sum(M1), sum(M2), sum(M3)))
print()
print("每台机器完成的作业：")
for num, j in enumerate(M):
    print("机器{}：".format(num + 1), end='')
    for k in j:
        print("作业{}".format(tasks[k]), end=',')
    print()
