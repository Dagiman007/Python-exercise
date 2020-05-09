def main():
    # Prompt the user to enter a phone number as a string
    phoneNumber = input('Enter a string: ').strip().upper()

    for char in phoneNumber:
        if not char.isalpha():
            print(char, end = '')
            continue
        else:
            print(getNumber(char), end = '')
    
            

# Change upper case letter to a number
def getNumber(uppercaseLetter):
    if 'A' <= uppercaseLetter <= 'C':
        return 2
    elif 'D' <= uppercaseLetter <= 'F':
        return 3
    elif 'G' <= uppercaseLetter <= 'I':
        return 4
    elif 'J' <= uppercaseLetter <= 'L':
        return 5
    elif 'M' <= uppercaseLetter <= 'O':
        return 6
    elif 'P' <= uppercaseLetter <= 'S':
        return 7
    elif 'T' <= uppercaseLetter <= 'V':
        return 8
    elif 'W' <= uppercaseLetter <= 'Z':
        return 9
    

main()  # Call the main function
