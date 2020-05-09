# The function for sorting elements in ascending order
def insertionSort(lst):
    for i in range(1, len(lst)):
        #insert lst[i] into a sorted sublist lst[0:i] so that
        # lst[0:i+1] is sorted
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1

        # Insert the current element into lst[k + 1]
        lst[k + 1] = currentElement

import random
from math import sqrt
def main():
    list1 = [format(sqrt(x),'.2f') for x in range(50)]
    random.shuffle(list1)
    print('Unsorted list\n',list1,'\n\n')
    insertionSort(list1)
    print('Sorted list\n',list1)

main()
        
