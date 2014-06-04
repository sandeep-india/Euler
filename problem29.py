'''
Distinct powers

'''
my_list = []

for i in range(2,101):
	for j in range(2,101):
		number = pow(i,j)
		if number not in my_list:
			my_list.append(number)

print "Total distinct powers", len(my_list)
