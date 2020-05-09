''' A program that gives a real solution to
quadratic equation by first checking its
discriminant '''

import math

#Prompt the user to enter the coefficeints of the quadratic equation
a,b,c = eval(input("Enter the coefficients a,b,c in ax^2 + bx + c: "))

#calculate the discriminant
discriminant = math.pow(b,2) - 4*a*c

#check the discriminant
if discriminant > 0 :
    root1 = (-b - math.sqrt(discriminant))/(2*a)
    root2 = (-b + math.sqrt(discriminant))/(2*a)
    print("The quadratic equation has two real roots, r1 =",round(root1,5)," and r2 =",round(root2,5))
elif discriminant == 0:
    root = -b/(2*a)
    print("The equation has only one real root, r =",round(root,5))
else:
    print("The equation has on real root")
    
