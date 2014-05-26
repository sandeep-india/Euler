'''

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

sumsquare = 0
squaresum = 0
diff = 0
for i in range(1,101):
	squaresum = squaresum + (i*i)
	sumsquare = sumsquare + i

sumsquare = sumsquare*sumsquare
diff = (sumsquare - squaresum)
print diff