# python3 学习笔记

## Python基础

### 循环
	
* `for...in`

	`for...in`循环，可以依次遍历`list`、`range`或者`tuple`等数据结构中的每个元素。

		>>> nbaStar = ["Kobe", "Duncun", "Curry", "Wade"]
			for name in nbaStar:
				print("\t", name)
   
   				Kobe
	 			Duncun
	 			Curry
	 			Wade

		>>> sum = 0
			for x in range(101):  # range(n)生成一个[0,n)整数序列
    			sum += x
			print("the sum of 1~100 :", sum)
			
			the sum of 1~100 : 5050

* `while`

	只要条件满足，就不断循环，条件不满足时退出循环。
	
		>>> sum = 0
			n = 100
			while n >= 0 :  # while循环，只要条件满足，就不断循环，条件不满足时退出循环。
    			if(n % 2 == 0):
        			sum = sum + n
    			n = n - 1
			print("the sum of all odd numbers in 1~100 :", sum)
			
			the sum of all odd numbers in 1~100 : 2550

* `break`

	跳出循环，即结束当前循环
	
		>>> n = 1
			while 1:
    			if n > 10:
        			break
    			print("\t", n)
    			n = n + 1
			print("END")
			
				 1
				 2
				 3
				 4
				 5
				 6
				 7
				 8
				 9
				 10
	
* `continue`

	结束当前单次循环，快速进入下一次循环
	
		>>> n = 0
			while n < 10:
    			n = n + 1
    			if n % 2 == 0:
        			continue 
		    	print("\t", n)
		    
		    	 1
	 			 3
	 			 5
	 			 7
	 			 9
