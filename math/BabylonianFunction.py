def main():
    n = eval(input('Enter a number: '))

    print('The square root of {} is {}'.format(n, sqrt(n)))

def sqrt(n):
    e = 0.00001
    lastGuess = 1
    nextGuess = n
    while lastGuess != nextGuess:
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        if abs(lastGuess - nextGuess) < e:
            break
        nextGuess, lastGuess = lastGuess, nextGuess

    return nextGuess

main()
    
