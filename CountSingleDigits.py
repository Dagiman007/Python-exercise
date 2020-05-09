from random import randint

def main():
    numbers = []
    for i in range(1000):
        numbers.append(randint(0, 9))

    counts = countDigits(numbers)
    for i in range(10):
        print('Number of {}s is '.format(i), counts[i])

def countDigits(numbers):
    counts = [0]*10

    for number in numbers:
        counts[number] += 1

    return counts
    
    
main()
