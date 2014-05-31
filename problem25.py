'''

Thousand-digit Fibonacci number

'''

a = 1
b = 1
length = 1
term = 2
while length < 1000:
	c = a+b
	a,b = b,c
	#print b
	length = len(str(b))
	term += 1
print term