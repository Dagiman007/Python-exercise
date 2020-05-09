#keep the program running after an exception
'''
while True:
    try:
        a = int(input('First number: '))
        b = int(input('Second number: '))
        print('Your result is ',a/b)
    except:
        print('Invalid input. Please retry.')
    else:
        break
'''

#using finally to clean up after an exception

def divlog(x,y):
    try:
        f = open('C:/Users/DagiMan/Desktop/Python Programming - CBT Nuggets/Exercise/spam.txt','a')
        f.write('{0:g}/{1:g} = {2:g}\n'.format(x,y,(x/y)))
    except ZeroDivisionError:
        f.write('Error: zero division not allowed\n')
        raise
    finally:
        f.close()
        
