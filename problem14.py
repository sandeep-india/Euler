'''

(Collatz Problem)

'''

def collatz(n):
	sum = 1
	while n>1:
		sum += 1
		if not n & 1:
			n = n/2
		else:
			n = (3*n+1)
	return sum

highest = 0
k = 0 
for i in range(1,1000001):
	number = collatz(i)
	print number
	if number > highest:
		highest = number
		k= i



print k