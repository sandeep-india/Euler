'''

Thousand-digit Fibonacci number

'''

import time

start = time.time()


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

elapsed = time.time() - start

print("found in %s seconds") % elapsed