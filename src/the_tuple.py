#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年11月16日

@author: taomk
'''
classmates = ('Kobe', 'Duncun', 'James') #定义一个tuple
print(classmates)
print("获取tuple的元素个数：", len(classmates))
print("通过索引（0-based）来访问tuple中元素：", classmates[0])
# print("通过索引（0-based）来访问tuple中元素：", classmates[3]) # IndexError: tuple index out of range
print("通过索引（0-based）来访问tuple中元素，获取最后一个元素：", classmates[-1])
# print("通过索引（0-based）来访问tuple中元素：", classmates[-4]) # IndexError: tuple index out of range

t1=(1)
print("此时t1是一个数", t1)

t2=(1,)
print("此时t2是一个tuple", t2)