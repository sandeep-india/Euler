'''

Work out the first ten digits of the sum of the following one-hundred fifty-digit numbers.

'''

import os
fin = open(os.path.expanduser("~/Documents/euler/problem13.data"), "r")
rows = [line.strip() for line in fin.readlines()]
sum = 0
for row in rows:
	number = int(row)
	sum = sum + number

print sum