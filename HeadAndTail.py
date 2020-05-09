from random import randint

def main():
    num = eval(input('Enter a number between 0 and 511: '))
    binary = decimalToBinary(num)
    while len(binary) < 9:
        binary = '0' + binary

    display(binary)

# Convert decimal to binary as a string
def decimalToBinary(value):
    binary = ''
    while value != 0:
        remainder = value % 2
        binary = str(remainder) + binary
        value = value // 2

    return binary

def display(m):
    count = 0
    for ch in m:
        if count % 3 == 0:
            print()
        if ch == '0':
            print('H', end = ' ')
        elif ch == '1':
            print('T', end = ' ')
        count += 1

main()
        
