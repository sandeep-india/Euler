'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


'''


def lprimefac(k):
	large = 1
	for i in range(2,((k/2)+1)):
		if k%i == 0:
			k= k/i
			large = i
	return large


print "%d" %(lprimefac(13195))


'''

This example depicts how computers can solve probems which take horrible amouths of time for humans to solve, Try solving this manually :P
Note that the total loop iterations are (K/2+1)

'''
