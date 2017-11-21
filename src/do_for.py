#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年11月21日

@author: taomk
'''
print("NBA Star :")
nbaStar = ["Kobe", "Duncun", "Curry", "Wade"]
for name in nbaStar:  # for...in循环，依次遍历list、range或者tuple等中的每个元素
    print("\t", name)

print("=================")

sum = 0
for x in range(101):  # range(n)生成一个[0,n)整数序列
    sum += x
print("the sum of 1~100 :", sum)

print("=================")

sum = 0
n = 100
while n >= 0 :  # while循环，只要条件满足，就不断循环，条件不满足时退出循环。
    if(n % 2 == 0):
        sum = sum + n
    n = n - 1
print("the sum of all odd numbers in 1~100 :", sum)

print("=================")

print("COUNT <=10 NUMBERS START")
n = 1
while 1:
    if n > 10:
        break  # break会跳出循环，即结束当前循环
    print("\t", n)
    n = n + 1
print("END")

print("=================")

print("COUNT ODD NUMBERS（<10） START")
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue  # continue会结束当前单次循环，快速进入下一次循环
    print("\t", n)
print("END")

