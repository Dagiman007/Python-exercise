def main():
    index = eval(input('Enter an index for a Fibonnaci number: '))
    # Find and display the fibonnaci number
    print('The fibonnaci number at index ', index, ' is ', fib(index))

# The function for finding the Fibonnaci number
def fib(index):
    if index == 0:  # Base case
        return 0
    elif index == 1:  # Base case
        return 1
    else:
        return fib(index - 1) + fib(index - 2)

main()
