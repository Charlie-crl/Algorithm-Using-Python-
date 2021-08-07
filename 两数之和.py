# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：两数之和
@时间：2020/3/1  
"""
#题目：
#给定一个nums数组和目标值target
#请你在该数组中找出和为目标值的那两个整数
#返回他们的数组下标
#采用哈希表法

nums = [2,7,11,15,4,5,3,6]
target = 9
result = {}
index_List = []
for i,num in enumerate(nums):
    temp = target - num
    if temp in result :
        index_List = index_List + [[result[temp]] + [i]]
    result[num] = i

print(index_List)
print(result)



