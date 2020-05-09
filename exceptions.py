'''
try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print("Your result is ",a/b)
except ZeroDivisionError:
    print('Erro: Division by zero will not work.')
'''
'''
try:
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print('your result is ',a/b)
except ZeroDivisionError:
    print('Division by zero will not work')
except ValueError,IOError:
    print('Invalid input')
'''
'''
try:
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print('your result is ',a/b)
except (ZeroDivisionError,ValueError,TypeError): #Tuple
    print('Invalid input detected')
'''
#mor dynamic exception message text
try:
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print('your result is ',a/b)
except (ZeroDivisionError,ValueError,TypeError) as e:
    print('Error: ',e)
    
    

