# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：整数划分
@时间：2020/3/12  
"""

# 用python字典这个数据结构存储划分因子，从1开始，用0占位
dividing_number = {0: 0}
# 次数累加变量
times = 0


def int_divide(number, index):
    global times
    # 从1开始遍历该整数所有划分因子
    for i in range(1, number+1):
        # 与前一位划分因子比较，去重，如先有24,42则不行
        if i >= dividing_number[index-1]:
            dividing_number[index] = i
            # 当前数-划分因子后还剩数，如6-1剩5
            number_rest = number - i
            # 整数被划分完毕
            if number_rest == 0:
                # 输出划分因子
                for j in range(1, index):
                    print(str(dividing_number[j])+'+', end='')
                print(str(dividing_number[index]))
                times = times + 1
            # 未被划分完毕，继续，dividing_Number划分位数+1
            else:
                int_divide(number_rest, index+1)
        else:
            pass


n = int(input("请输入一个整数\n"))
int_divide(n, 1)
print("所以该整数的划分数为：%d" % times)
