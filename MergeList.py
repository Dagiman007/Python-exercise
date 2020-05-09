
def main():
    list1 = [eval(x) for x in input('Enter list1: ').split()]
    list2 = [eval(x) for x in input('Enter list2: ').split()]

    mergedList = merge(list1, list2)

    print('The merged list is ', end = '')
    for number in mergedList:
        print(number, end = ' ')

def merge(list1, list2):
    list1.extend(list2)
    list1.sort()

    return list1

main()
    
                
