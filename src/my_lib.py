'''
自定义的函数库

Created on 2017年12月22日

@author: taomaokun
'''
import math

#===============================================================================
# 自定义abs(x)函数
#===============================================================================
def my_abs(x):
#参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x;
    else:
        return -x;

#===============================================================================
# move 返回移动后的坐标
#===============================================================================
def move(x, y, step, angle=0):
    new_x = x + step*math.cos(angle)
    new_y = y + step*math.sin(angle)
    return new_x, new_y
