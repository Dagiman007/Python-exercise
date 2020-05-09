def main():
    n = eval(input('Enter a nonnegative integer: '))
    print('Factorial of ', n, ' is ', factorial(n))

# Return the factorial for the specified number
def factorial(n):
    return n * factorial(n - 1) if n > 0 else 1


main()
