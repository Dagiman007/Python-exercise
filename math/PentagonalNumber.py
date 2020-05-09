def main():
    # Prompt the user to enter n
    n = eval(input('Enter n: '))

    # Get the first n pentagonal numbers
    for i in range(1, n + 1):
        print(format(getPentagonalNumber(i),'5.0f'),end = ' ')
        if i % 10 == 0:
            print()
        
def getPentagonalNumber(n):
    return n*(3*n - 1)/2

main() # Call the main function
