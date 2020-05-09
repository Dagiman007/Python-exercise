import cmath

x = 1.0
y = 0.0

z = complex(x, y)

# Printing the phase of a complex number using phase()
print('The phase of complex number is: ', end = '')
print(cmath.phase(z))

z = complex(1.0, 1.0)

w = cmath.polar(z) # Convert into polar
print('The modulus and argument of polar complex number is: ', end = '')
print(w)

w = cmath.rect(1.4142135623730951, 0.7853981633974483)  # Convert into rectangular using rect()

print('The rectangular form of complex number is: ', end = '')
print(w)

x = 1.0
y = 1.0
z = complex(x, y)

# Printing the exponent of complex number
print('The exponent of complex number is: ', end = '')
print(cmath.exp(z))

# Printing log form of complex number
print('The natural log of complex number is: ', end = '')
print(cmath.log(z))

# Printing log 10 of complex number
print('The log 10 of complex number is: ', end = '')
print(cmath.log10(z))

# Printing square root of complex number
print('The square root of complex number is: ', end = '')
print(cmath.sqrt(z))

