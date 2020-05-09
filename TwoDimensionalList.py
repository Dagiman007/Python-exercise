matrix = []

numberOfRows = eval(input('Enter the number of rows'))
numberOfColumns = eval(input('Enter the number of columns'))

for row in range(numberOfRows):
    matrix.append([])
    for column in range(numberOfColumns):
        value = eval(input('Enter an element and press enter: '))
        matrix[row].append(value)

import random
matrix1 = []
for row in range(numberOfRows):
    matrix1.append([])   # Add an empty new row
    for column in range(numberOfColumns):
        matrix[row].append(random.randint(0,99))


for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column])


# Summing all elements
total = 0
for row in matrix:
    for value in row:
        total += value

# Summing elements by column
for column in range(len(matrix[0])):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][column]
    print('Sum for column ',column,'is',total)



        
