# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：入门训练之求圆的面积
@时间：2020/3/4  
"""
"""
1. 数字的四舍五入
当我们需要对整数 或者 浮点数进行四舍五入的时候。
round(value, ndigits)  /// 内置函数
对浮点数进行四舍五入(传入的ndigit应该是正值，作用于十分位、百分位...)：
print( round(1.23, 1) )     # 1.2
print( round(1.27, 1) )     # 1.3
print( round(-1.27, 1) )    #-1.3
print( round(1.25361, 3))   #1.254
print( round(2.5, 0) )      #2.0 近似到最近的偶数
对整数进行四舍五入(传入的ndigit应该是自然数，作用于个位、十位、百位...)
print( round(314159, -1))    #314160
print( round(314159, -2))    #314200
print( round(314159, -3))    #314000
Comment：

不要将舍入round和格式化format输出搞混淆了。 如果我们目的只是简单的输出一定宽度的数，不需要使用 round() 函数。 而仅仅只需要在格式化的时候指定精度即可。

pi = 3.1415926
print( format(pi, '0.2f')) #3.14
print( format(pi, '0.3f')) #3.142
print( 'the value is {:0.4f}'.format(pi) ) #the value is 3.1416
print(format(x, '>10.1f'))   #'    1234.6'
print(format(x, '<10.10f'))  #'1234.5678900000'
print(format(x, '^10.1f'))   #'  1234.6  '
print(format(x, ','))        #1,234.56789
print(format(x, 'e'))        #1.234568e+03科学计数法
print('The value is {:0,.2f}'.format(x)) # The value is 1,234.57

"""

import math
r = int(input())
s = r*r*math.pi
print(format(s, '0.7f'))
print(f"{s:0.7f}")

