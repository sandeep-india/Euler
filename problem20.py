'''

Factorial digit sum

'''

from math import factorial
number = str(factorial(100))
length = len(number)
sum=0
for i in range(0,length):
	sum = sum+int(number[i])

print sum