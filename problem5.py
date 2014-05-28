'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''


def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def lprimefac(k):
	large = 1
	if isprime(k):
		large = k
	else:
		p = k	
		for i in range(2,(k/2+1)):
			if p%i == 0:
				p= p/i
				if isprime(i):
					large = i
	return large


number = 1
final = 1
till = 21
factors = []
factors1 = []
for i in range(1,till):
	if (number%i) != 0:
		if lprimefac(i) in factors:
			print 'pass %d' %i
		else:
			number = number*lprimefac(i)
			factors.append(lprimefac(i))
	else:
		print 'pass %d' %i


for n in factors:
	p = n
	while n < till:
		n = n*p
	factors1.append(n/p)

for n in factors1:
	final = final*n


print number
print factors
print factors1
print final

