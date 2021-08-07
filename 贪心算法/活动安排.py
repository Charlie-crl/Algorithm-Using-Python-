# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：活动安排
@时间：2020/4/22  
"""

"""
问题描述：
设有n个活动的集合E={1,2,...,n}，其中每个活动都要求使用同一资源，如演讲会场等，
而在同一时间内只有一个活动能使用这一资源。每个活动i都有一个要求使用该资源的起始时间si和一个结束时间fi，且si<fi。
"""

# 数据准备：
# 从结束时间最早的活动开始安排
a = [1]
fi = 4
# 设有11个活动，且已按fi增序的形式排序
activities = {
    # fi : si
    4: 1,
    5: 3,
    6: 0,
    7: 5,
    8: 3,
    9: 5,
    10: 6,
    11: 8,
    12: 8,
    13: 2,
    14: 12
}
# 总体算法
for item, fj in enumerate(activities):
    if fj == 4:
        continue
    sj = activities[fj]
    # 满足：当前sj >= 上次已安排活动的fi?
    if sj >= fi:
        fi = fj
        # 记录
        a.append(item + 1)
    else:
        pass
# 输出一个最优解
print("最优活动安排顺序为：")
for i in a:
    print("活动i = %d" % i)
