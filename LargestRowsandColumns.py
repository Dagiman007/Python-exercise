from random import randint

def main():
    matrix = []
    for i in range(4):
        matrix.append([])
        for j in range(4):
            matrix[i].append(randint(0, 1))

    display(matrix)
    print('The largest row index: ', largestRowIndex(matrix))
    print('The largest column index: ', largestColumnIndex(matrix))

def display(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end = ' ')
        print()
        
def largestRowIndex(m):
    count = [0]*len(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                count[i] += 1

    return count.index(max(count))

def largestColumnIndex(m):
    count = [0]*len(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                count[j] += 1

    return count.index(max(count))

main()
