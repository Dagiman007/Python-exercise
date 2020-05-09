#Prompt the user to enter to positive integers
n1,n2 = eval(input("Enter two positive integers n1,n2: "))

gcd = 1
k = 2

while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k += 1

if gcd == 1:
    print("The two numbers are relatively prime numbers, i.e. GCD = 1")
else:
    print("The GCD of ",n1," and ",n2," is ",gcd)
