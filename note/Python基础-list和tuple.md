# python3 学习笔记

## Python基础

### list
	
Python内置的一种数据类型，它是一种有序的集合，可以随时添加和删除其中的元素。

	>>> classmates = ['Kobe', 'Duncun', 'James'] #申明一个list
	>>> print(classmates)
	['Kobe', 'Duncun', 'James']
	
	>>> print("获取list的元素个数：", len(classmates))
	获取list的元素个数： 3
	
	>>> print("通过索引（0-based）来访问list中元素：", classmates[0])
	通过索引（0-based）来访问list中元素： Kobe
	
	>>> print("通过索引（0-based）来访问list中元素：", classmates[3]) 
	IndexError: list index out of range
	
	>>> print("通过索引（0-based）来访问list中元素，获取最后一个元素：", classmates[-1])
	通过索引（0-based）来访问list中元素，获取最后一个元素： James
	
	>>> print("通过索引（0-based）来访问list中元素：", classmates[-4]) 
	IndexError: list index out of range
	
	>>> print("追加元素到list末尾：", classmates.append("Wade"), classmates)
	追加元素到list末尾： None ['Kobe', 'Duncun', 'James', 'Wade']
	
	>>> print("插入元素到指定位置:", classmates.insert(1, "Jordan"), classmates)
	插入元素到指定位置: None ['Kobe', 'Jordan', 'Duncun', 'James', 'Wade']
	
	>>> print("删除指定位置的元素:", classmates.pop(2), classmates)
	删除指定位置的元素: Duncun ['Kobe', 'Jordan', 'James', 'Wade']
	
	>>> classmates[3] = "Park"
	>>> print("修改指定位置的元素:", classmates)
	修改指定位置的元素: ['Kobe', 'Jordan', 'James', 'Park']
	
	>>> anotherClassmates = ['Java', 666, True]
	>>> classmates[2] = anotherClassmates
	>>> print("list的元素可以是另一个list:", classmates)
	list的元素可以是另一个list: ['Kobe', 'Jordan', ['Java', 666, True], 'Park']
	
	>>> print("此时访问插入的list的元素:", classmates[2][1])
	此时访问插入的list的元素: 666

### tuple
另一种有序列表叫**元组**：`tuple`。`tuple`和`list`非常类似，但是**tuple一旦初始化就不能修改**。


	