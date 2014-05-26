'''

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc

'''

for a in range (1,1000):
	for b in range(1,1000):
		for c in range(1,1000):
			if a+b+c == 1000:
				if ((a*a)+(b*b) == (c*c)):
					print a
					print b
					print c
					print (a*b*c)
					break
					break
					break

'''

Not sure how to break, find out

'''