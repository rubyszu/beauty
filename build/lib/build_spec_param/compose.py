import functools

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
	runner = compose([add, minus, double])
	# double(minus(add(x)))
	print(runner(3))