'''
sum of primes under two million

'''

sum = 0

def isprime(n):
	prime = True
	for i in range(2,n):
		if n%i == 0:
			prime = False 
	return prime

for i in range(0,2000000):
	if isprime(i):
		sum = sum+i
		print sum

print sum
