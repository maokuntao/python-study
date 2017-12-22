'''
Created on 2017年12月22日

@author: taomaokun
'''
# 要创建一个set，需要提供一个list作为输入，重复元素在set中自动被过滤
s = set([1, 2, 3, "3", "Python", True, False, 233, 233])
print(s)

# 添加元素
s.add("Java")
print(s)

# 删除元素
s.remove(233)
print(s)

# KeyError
# s.remove("PHP")
# print(s)

s2 = set([2, 3, 4, 5])
# 计算交集
print(s & s2)
# 计算并集
print(s | s2)
