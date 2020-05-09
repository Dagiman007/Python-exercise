def main():
    numbers = [eval(x) for x in input('Enter numbers: ').split()]

    bubblesort(numbers)

    for number in numbers:
        print(number, end = ' ')

def bubblesort(lst):
    needNextPass = True

    while len(lst) > 1 and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False

        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

                needNextPass = True  # Next pass still needed

main()
