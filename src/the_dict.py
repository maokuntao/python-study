#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Created on 2017年12月20日

@author: taomk
'''
# 定义一个dict
number_name_dict = {"Jordan":23, "Kobe":8, "Duncan":21, "Parker":9}
print(number_name_dict["Duncan"])

# 给dict中的item赋值
number_name_dict["Kobe"] = 24
number_name_dict["Paul"] = 3
print(len(number_name_dict))
print(number_name_dict)

# 如果key在dict中不存在，会返回一个KeyError
# print(number_name_dict["Yao"])

if("Yao" in number_name_dict):
    print(number_name_dict)
else:
    print("'Yao' is not in dict")
    number_name_dict["Yao"] = 11

if(number_name_dict.get("Yao")):
    print(number_name_dict)
else:
    print("'Yao' is not in dict still")
    
if(number_name_dict.pop("Yao")):
    print(number_name_dict)
else:
    print("'Yao' is not in dict again")