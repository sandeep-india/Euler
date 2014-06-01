import time

start = time.time()

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

def quad(a,b):
    n=0
    con = 0
    prime = True
    while prime:
        number = n**2+a*n+b
        prime = isprime(number)
        n +=1
        con += 1
        print con
    return con

highest = 0
product = 0
for b in range(1,1000):
    for a in range(-999,1000):
        if isprime(b):
            count = quad(a,b)
            if count > highest:
                highest = count
                product = a*b

print "The highest consucutive primes are %s" %str(highest)
print "The highest product is %s" %str(product)

executed_in = time.time() - start

print "Executed in %s secs" %executed_in

