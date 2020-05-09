''' The program uses the Sieve of Eratosthenes
algorithm to find prime numbers
'''

n = int(input("Enter a number: "))

def erathostenes(n):
    not_prime = { j for i in range(2,n)
                  for j in range(i*2,n,i)
                }
    return {i for i in range(2,n)
            if i not in not_prime
            }

primeNumbers = erathostenes(n)

print("The prime numbers upto ",n," are ",primeNumbers)
