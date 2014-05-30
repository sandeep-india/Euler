'''
Lexicographic permutations.

'''
import time

start = time.time()

from math import factorial

my_list = [i for i in range(0,10)]
fac_list = [factorial(i) for i in range(10)]
factor_list = []
number=''

index = 999999

for i in range(9,-1,-1):
	factor_list.append(index/fac_list[i])
	index = index % fac_list[i]

for i in range(0,10):
	number += str(my_list[factor_list[i]])
	my_list.pop(factor_list[i])

print number

elapsed = time.time() - start

print("found in %s seconds") % elapsed
