import time
start = time.time()

n = 1
squares = range(1,1002,2)
length = len(squares)
Total = 1
for i in range(1,length):
	for j in range(0,4):
		Total += (squares[i]**2) - (j*i*2)

print Total

executed_for = time.time() - start

print "Solved in %s seconds" %executed_for