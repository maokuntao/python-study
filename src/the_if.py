#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年11月16日

@author: taomk
'''
from math import pow

height = input("Your height (m) : ")
weight = input("Your weight (kg) : ")

# input()返回的数据类型是str，必须先把str转换成float
bmi = float(weight)/pow(float(height), 2)

# 只要bmi是非零数值、非空字符串、非空list等，就判断为True，否则为False
if bmi:
    print("Your BMI :", bmi)
# 条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行
if bmi<18.5:
    print("过轻")
elif bmi<25:
    print("正常")
elif bmi<28:
    print("过重")
elif bmi<32:
    print("肥胖")
else:
    print("过于肥胖")