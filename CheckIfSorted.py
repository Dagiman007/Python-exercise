def main():
    x = [eval(x) for x in input('Enter list: ').split()]

    if isSorted(x):
        print('The list is sorted')
    else:
        print('The list is not sorted')

def isSorted(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[i + 1]:
                return False

    return True

main()
