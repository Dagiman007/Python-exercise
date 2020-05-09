#convert decimal to hex as a string
def decimalToHex(decimalValue):
    hex = ''
    while decimalValue != 0:
        hexValue = decimalValue % 16
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16

    return hex
#convert an integer to a single hex digit as a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:
        return chr(hexValue - 10 + ord('A'))

def main():
    #prompt the user to enter a decimal integer
    decimalValue = eval(input('Enter a decimal number: '))

    print('The hex number for decimal ',decimalValue,'is',decimalToHex(decimalValue))

main()
