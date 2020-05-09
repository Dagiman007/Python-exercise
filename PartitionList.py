def main():
    lst = [eval(x) for x in input('Enter a list: ').split()]

    partition(lst)

    print('After the partition, the list is ', end = '')
    for i in lst:
        print(i, end = ' ')

def partition(lst):
    pivot = lst[0]  # Choose the first element as the pivot
    low = 1  # Index for forward search
    high = len(lst) - 1  # Index for backward search

    while high > low:
        # Search forward from left
        while low <= high and lst[low] <= pivot:
            low += 1

        # Search backward from right
        while low <= high and lst[high] > pivot:
            high -= 1

        # Swap two elements in the list
        if high > low:
            lst[high], lst[low] = lst[low], lst[high]

    while high > 1 and lst[high] >= pivot:
        high -= 1

    # Swap pivot with list[high]
    if pivot > lst[high]:
        lst[0] = lst[high]
        lst[high] = pivot

main()
        
