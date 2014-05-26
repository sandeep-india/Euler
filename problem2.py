'''

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''
current_fabo = 2
previous_fabo = 1
sum = 0
while (current_fabo < 4000000):
	if current_fabo%2 == 0:
		print sum
		sum = sum + current_fabo
	new_fabo = current_fabo + previous_fabo
	previous_fabo = current_fabo
	current_fabo = new_fabo

print sum



