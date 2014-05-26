#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is Find the largest palindrome made from the product of two 3-digit numbers.
large = 0
for i in range(100,1000):
	for j in range(100,1000):
		num = i*j
		if str(num) == str(num)[::-1]:
			if num > large:
				large = num
print large
