def main():
    # Prompt the user to enter password
    password = input('''Enter password: \nThe password must \n
    - have at least eight characters\n
    - consist of only letters and digits\n
    - contain at least two digits\n''').strip()

    if isValid(password):
        print('Valid password')
    else:
        print('Invalid password')


def isValid(passwd):
    if len(passwd) < 8:
        return False  # Invalid number of characters
    
    numberOfDigits = 0
    
    for char in passwd:
        if (not char.isalpha()) or (not char.isdigit()):
            return False   # Include invalid characters
            break
        elif char.isdigit():
            numberOfDigits += 1
            
    if numberOfDigits < 2:
        return False  # less number of digits
    else:
        return True  # Valid password

    
main()
