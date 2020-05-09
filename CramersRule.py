'''A program that uses the cramer's rule
to solve 2x2 systems of linear equation '''

#prompt the user to enter the coefficients
print("The program solves the system of equation\n \
\tax + by = e\n\
\tcx + dy = f\n")
a,b,c,d,e,f = eval(input("Enter a,b,c,d,e,f: "))

denom = a*d - b*c
if denom == 0:
    print("The equation has no solution!")
else:
    x = (e*d - b*f)/denom
    y = (a*f - e*c)/denom
    print("x =",x," and y = ",y," is the solution")
                   
