'''

Amicable numbers

'''
import time

start = time.time()

p = 10000
my_list = []

for i in range(0,p):
	sum = 0

	for j in range(1,i):
		if i%j == 0:
			sum += j

	sum1 = 0
	for k in range(1,sum):
		if sum%k == 0:
			sum1 += k 

	if sum1 == i:
		my_list.append(i)
		#print my_list

my_list1 = list(set(my_list))

sum2 = 0
for number in my_list1:
	sum2 += number

elapsed = time.time() - start

print("found in %s seconds") % elapsed

print sum2
