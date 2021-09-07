# # def decor1(func):
# # 	def inner():
# # 		x = func()
# # 		return x*x
# # 	return inner

# # def decor(func):
# # 	def inner():
# # 		x = func()
# # 		return 2 * x
# # 	return inner

# # @decor1
# # @deco
# r# def num():
# # 	return 10


# def decor(func):
# 	def inner(a,b):
# 		if a < b:
# 			a, b = b, a
# 		return func(a,b)
# 	return inner

# @decor
# def div(a,b):
# 	print (a/b)

# div(2,4)

def decor(func):
	def adder(a,b,c):
		if a > b:
			print(c)
		else:
			print(b)
		return func(a,b,c)
	return adder


@decor
adder(1,2,4):