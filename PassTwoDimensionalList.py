import random
def getMatrix():
    numberOfRows = eval(input('Enter number of rows: '))
    numberOfColumns = eval(input('Enter the number of columns: '))
    matrix = []
    for row in range(numberOfRows):
        matrix.append([])   # Add an empty new row
        for column in range(numberOfColumns):
            matrix[row].append(random.randint(0,99))

    return matrix

def accumulate(m):
    total = 0
    for row in m:
        total += sum(row)

    return total

def main():
    m = getMatrix()
    print(m)

    print('\nSum of all elements is ',accumulate(m))

main()
