'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''
def isprime(n):
	prime = True
	for i in range(2,n):
		if n%i == 0:
			prime = False 
	return prime


index = 0
number = 0
while (index < 10002):
	print index
	number = number+1
	if isprime(number):
		index = index + 1

print number


