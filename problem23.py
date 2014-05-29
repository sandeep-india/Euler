import time

start = time.time()


upper = 28123
abundant_list = []
abundant_sums = []

for i in range(0,upper+1):
	sum = 0
	for j in range(1,i):
		if i%j == 0:
			sum += j

	if sum > i:
		print i
		abundant_list.append(i)

length = len(abundant_list)
print "list lenghth is %s" %str(length)


for i in range(0,length):
	for j in range(0,length):
		sum1 = abundant_list[i]+abundant_list[j]
		if sum1 <= upper:
			#print sum1
			abundant_sums.append(sum1)

print 'next for loop done moving to total'

abundant_sums = list(set(abundant_sums))

total = 0
for i in range(0,upper+1):
	if not i in abundant_sums:
		total += i

print total

elapsed = time.time() - start

print("found in %s seconds") % elapsed