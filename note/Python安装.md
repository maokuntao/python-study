# python3 学习笔记

## Python安装

> Python是跨平台的，它可以运行在Windows、macOS和各种Linux/Unix系统上。在一个平台上编写的Python代码，在其它平台上也可以运行（Python版本一致，而且解释器一致）。

* 版本

	目前，Python有两个版本，一个是2.x版，一个是3.x版，这两个版本是不兼容的。
	
	*23333，看看我大Java，😂*

* Python解释器
> 当我们编写Python代码时，我们得到的是一个包含Python代码的以.py为扩展名的文本文件。要运行代码，就需要Python解释器去执行.py文件。
> 由于整个Python语言从规范到解释器都是开源的，所以理论上，只要水平够高，任何人都可以编写Python解释器来执行Python代码（当然难度很大）。事实上，确实存在多种Python解释器。


	* CPython 
	
		官方版本的解释器，这个解释器是用C语言开发的，所以叫CPython。在命令行下运行python就是启动CPython解释器。
CPython是使用最广的Python解释器。
	
	* IPython
	
		基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强。CPython用`>>>`作为提示符，而IPython用`In [序号]:`作为提示符。
		
	* PyPy
	
		另一个Python解释器，它的目标是执行速度。PyPy采用 [JIT](https://en.wikipedia.org/wiki/Just-in-time_compilation) 技术，对Python代码进行动态编译（注意不是解释），所以可以显著提高Python代码的执行速度。
		
	* Jython
	
		运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。
		
		*蛤？wtf*
		
	* IronPython
		
		和Jython类似，只不过IronPython是运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。
		
		*好吧*