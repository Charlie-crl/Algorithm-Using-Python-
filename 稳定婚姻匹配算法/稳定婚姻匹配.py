# -*- encoding:utf-8 -*-
"""
@作者：陈润林
@问题名：稳定婚姻匹配
@时间：2020/2/28  
"""

"""
boys_loveSort = [
    ['Xavier','Amy','Bertha','Clare',0],
    ['Yancey','Bertha','Amy','Clare',0],
    ['Zeus','Amy','Bertha','Clare',0]
]
girls_loveSort = [
    ['Amy','Yancey','Xavier','Zeus',0],
    ['Bertha','Xavier','Yancey','Zeus',0],
    ['Clare','Xavier','Yancey','Zeus',0]
]
love_Situation = [
    ['Xavier',"no girl"],
    ['Yancey',"no girl"],
    ['Zeus',"no girl"]
]
"""


# 用0,1代表配对情况
# 查找女生单身状况
def find_Girl_state(girl_Name):
    for girl in girls_loveSort:
        if girl[0] == girl_Name:
            return girl[-1]


# 两人牵手成功
def marry(man, woman):
    man[-1] = 1
    for girl in girls_loveSort:
        if girl[0] == woman:
            girl[-1] = 1
    for man_Situation in love_Situation:
        if man_Situation[0] == man[0]:
            man_Situation[1] = woman


# 两人分手
def divorce(old_man):
    for man in boys_loveSort:
        if man[0] == old_man:
            man[-1] = 0
    for man2 in love_Situation:
        if man2[0] == old_man:
            man2[1] = "no girl"


# 两个男人竞争，看女人更喜欢谁
def complete(man, woman):
    old_Man = ""
    new_index = 0
    old_index = 0
    for partner in love_Situation:
        if partner[1] == woman:
            old_Man = partner[0]
    for girl in girls_loveSort:
        if girl[0] == woman:
            for index, husband in enumerate(girl):
                if husband == old_Man:
                    old_index = index
                elif husband == man[0]:
                    new_index = index
                else:
                    pass
    return [new_index < old_index, old_Man]


# 要输入分析的男女生资料
row_Number, col_Number = map(int, input("请输入表格的行数，列数（第一行不用，以空格隔开）\n").split())
boys_loveSort = []
girls_loveSort = []
love_Situation = []
for item in range(row_Number):
    boys_loveSort.extend([input("请输入男生喜爱表格，按行输入（第一行不用,以空格隔开）\n").split()])
    boys_loveSort[item].append(0)
for item in range(row_Number):
    girls_loveSort.extend([input("请输入女生喜爱表格，按行输入（第一行不用，以空格隔开）\n").split()])
    girls_loveSort[item].append(0)
for item in range(row_Number):
    a, *b = boys_loveSort[item]
    love_Situation.extend([[a, "no girl"]])

# 开始配对
for item in range(1, col_Number):
    for boy in boys_loveSort:
        if boy[-1] == 1:
            continue
        girl_State = find_Girl_state(boy[item])
        if girl_State == 0:
            marry(boy, boy[item])
        elif complete(boy, boy[item])[0] == True:
            marry(boy, boy[item])
            divorce(complete(boy, boy[item])[1])
        else:
            pass
# 结果
print(love_Situation)
