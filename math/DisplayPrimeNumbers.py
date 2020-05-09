'''A program that calculates the first n
number of prime numbers '''


#prompt the user to enter n
numberOfPrimes = eval(input("Enter the first number of primes you want to find: "))

count = 0
number = 2

print("The first ",numberOfPrimes," prime numbers are")

while count <= numberOfPrimes:
    isPrime = True
    divisor = 2
    while divisor <= number/2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1
    
    if isPrime:
        count += 1
        print(format(number,"5d"),end ='')
        if count % 10 == 0:
            print()
    number += 1

