def main():
    numbers = [eval(x) for x in input('Enter numbers: ').split()]

    print('Their GCD is ', gcd(numbers))

def gcd(numbers):
    g = numbers[0]
    for i in range(1, len(numbers)):
        g = gcd2(g, numbers[i])

    return g

# Return the gcd of two integers 
def gcd2(n1, n2):
    g = 1 # Initial gcd is 1
    k = 2   # Possible gcd

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            g = k # Update gcd
        k += 1

    return g # Return gcd

main()
