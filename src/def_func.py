'''
函数定义

Created on 2017年12月22日

@author: taomaokun
'''
from my_lib import my_abs

# print(my_abs('A')) #TypeError
# print(my_abs('-233'))#TypeError
print(my_abs(-233))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
another_my_abs = my_abs;
print(another_my_abs(-2.333))