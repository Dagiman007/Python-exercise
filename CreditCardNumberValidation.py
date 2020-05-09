def main():
    number = input('Enter the credit card number: ')

    if prefixMatched(number) and isValid(number):
        print('The card number ' + number + ' is valid')
    else:
        print('The card number ' + number + ' is invalid')

    
def isValid(number):
    sum = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    if sum % 10 == 0:
        return True
    else:
        return False
    
def sumOfDoubleEvenPlace(number):
    numberOfDigits = len(number)
    sum = 0
    for i in range(numberOfDigits-2,-1,-2):
        digit = 2*(eval(number[i]) )
        if digit >= 10:
            strDigit = str(digit)  
            digit = eval(strDigit[0]) + eval(strDigit[1])
        sum += digit
    return sum

def sumOfOddPlace(number):
    sum = 0
    numberOfDigits = len(number)
    
    for i in range(numberOfDigits-1,-1,-2):
        sum += eval(number[i])
    return sum

'''
def getDigit(number):
    return number if number < 10 else (number%10)+(number//10)'''
   

def prefixMatched(number):
    if number[0] == '4' or number[0] == '5' or number[0] == '6' or \
       (number[0] == '3' and number[0] == '7'):
        return True
    else:
        False
'''        
def getSize(d):
    print('A stub')

def getPrefix(number, k):
    print('A stub')'''



main()

