# python3 学习笔记

## Python基础

### if
	
在Python程序中，用`if`语句实现条件判断，让计算机自己根据满足的条件来执行不同的逻辑。

根据Python的缩进规则，如果`if`语句判断是`True`，就会执行缩进的语句，否则跳过缩进的内容往下执行，

条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的`elif`和`else`都不再执行。

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
	    
执行结果：

	Your height (m) : 1.75
	Your weight (kg) : 60
	Your BMI : 19.591836734693878
	正常
