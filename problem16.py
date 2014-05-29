'''
Power sum

'''

n = 1000
number = str(2**n)
length = len(number)
sum=0
for i in range(0,length):
	sum = sum+int(number[i])

print sum