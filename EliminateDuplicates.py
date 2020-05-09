def main():
    numbers = [eval(x) for x in input('Enter ten numbers: ').split()]

    print('The distinct numbers are ', end = ' ')
    distinctNumbers = eliminateDuplicates(numbers)
    for number in distinctNumbers:
        print(number, end = ' ')

def eliminateDuplicates(numbers):
    temp = []
    for number in numbers:
        if number in temp:
            continue
        else:
            temp.append(number)

    return temp

main()
