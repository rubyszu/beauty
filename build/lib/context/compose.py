# -*- coding: utf-8 -*-
import functools

# compose functions
def compose(functions):
    return functools.reduce(lambda prev, curr: lambda x: curr(prev(x)), functions, lambda x: x)

if __name__ == '__main__':
	def add(x):
		print("add")
		return x + 8

	def minus(x):
		print("minus")
		return x - 2

	def double(x):
		print("double")
		return x * 2
		
	# double(minus(add(x)))
	runner = compose([add, minus, double])
	print(runner(3))