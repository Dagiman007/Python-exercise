# International standard book number

def main():
    isbn = input('Enter the first 9 digits of an ISBN-10 as a string: ').strip()

    print('The ISBN-10 number is ', findISBN10(isbn))

def findISBN10(isbn):
    lastDigit = 0
    for i in range(len(isbn)):
        lastDigit += eval(isbn[i]) * (i + 1)
        
    lastDigit = lastDigit % 11

    isbn10 = isbn + ('X' if lastDigit == 10 else str(lastDigit))

    return isbn10

main()
        
    
