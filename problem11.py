'''
In the twenty grid below, four numbers along a diagonal line have been marked in red.

'''
import os

fin = open(os.path.expanduser("~/Desktop/euler/problem11.data"), "r")
rows = [line.strip() for line in fin.readlines()]
data = []
dummyrow =  [0]*26

for i in range(0,3):
    data.append(dummyrow)

for row in rows:
    row1=[]
    for i in range(0,3):
        row1.append(0)
    for element in row.split(" "):
        row1.append(int(element))
    for i in range(0,3):
        row1.append(0)

    data.append(row1)

for i in range(0,3):
    data.append(dummyrow)

till =len(data)

highest = 0

print data[3][3]

for i in range(0,till):
    for j in range(0,till):
      if i >= 3 and j >= 3 and j<=22 and i<=22:
        product = 1

        for k in range(0,4):
            product=data[i][j-k]*product

        if product > highest:
            highest = product

        product = 1
        for k in range(0,4):
            product=data[i][j+k]*product

        if product > highest:
            highest = product

        product = 1
        for k in range(0,4):
            product=data[i-k][j]*product

        if product > highest:
            highest = product

        product = 1
        for k in range(0,4):
            product=data[i+k][j]*product

        if product > highest:
            highest = product

        product = 1
        for k in range(0,4):
            product=data[i-k][j-k]*product

        if product > highest:
            highest = product

        product = 1
        for k in range(0,4):
            product=data[i+k][j+k]*product

        if product > highest:
            highest = product

        product = 1
        for k in range(0,4):
            product=data[i-k][j+k]*product

        if product > highest:
            highest = product     


        product = 1
        for k in range(0,4):
            product=data[i+k][j-k]*product

        if product > highest:
            highest = product    


print highest    