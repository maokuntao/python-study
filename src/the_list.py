#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年11月14日

@author: taomk
'''
classmates = ['Kobe', 'Duncun', 'James'] #申明一个list
print(classmates)
print("获取list的元素个数：", len(classmates))
print("通过索引（0-based）来访问list中元素：", classmates[0])
# print("通过索引（0-based）来访问list中元素：", classmates[3]) # IndexError: list index out of range
print("通过索引（0-based）来访问list中元素，获取最后一个元素：", classmates[-1])
# print("通过索引（0-based）来访问list中元素：", classmates[-4]) # IndexError: list index out of range
print("追加元素到list末尾：", classmates.append("Wade"), classmates)
print("插入元素到指定位置:", classmates.insert(1, "Jordan"), classmates)
print("删除指定位置的元素:", classmates.pop(2), classmates)
classmates[3] = "Park"
print("修改指定位置的元素:", classmates)
anotherClassmates = ['Java', 666, True]
classmates[2] = anotherClassmates
print("list的元素可以是另一个list:", classmates)
print("此时访问插入的list的元素:", classmates[2][1])