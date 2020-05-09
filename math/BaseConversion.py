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

# Convert hex to decimal as a string
def hexToDecimal(hex):
    decimalValue = 0
    for i in range(len(hex)):
        ch = hex[i]
        if ('A' <= ch <= 'F') or ('0' <= ch <= '9'):
            decimalValue = decimalValue * 16 + hexCharToDecimal(ch)
        else:
            return None
    return decimalValue

def hexCharToDecimal(ch):
    if 'A' <= ch <= 'F':
        return 10 + ord(ch) - ord('A')
    else:
        return ord(ch) - ord('0')

# Convert binary to decimal as a string
def binaryToDecimal(binaryString):
    decimal = 0
    length = len(binaryString)
    for binaryDigit in binaryString:
        decimal += eval(binaryDigit) * (2 ** (length - 1))
        length -= 1

    return str(decimal)

# Convert binary to hex as a string
def binaryToHex(binaryValue):
    length = len(binaryValue)
    hex = ''
    while length > 0:
        decimal = binaryToDecimal(binaryValue[length - 4: length])
        hex = toHexChar(int(decimal)) + hex
        length -= 4

    return hex


# Convert decimal to binary as a string
def decimalToBinary(value):
    binary = ''
    while value != 0:
        remainder = value % 2
        binary = str(remainder) + binary
        value = value // 2

    return binary

print(decimalToBinary(72))


        
