def main():
    # Prompt the user to enter social security number in the format ddd-dd-dddd
    ssn = input('Enter social security number, (e.g 345-22-7688): ').split('-')

    if isValid(ssn):
        print('Valid SSN')
    else:
        print('Invalid SSN')

def isValid(ssn):
    sum = 0
    for i in ssn:
        sum += len(i)
    if sum != 9:
        return False
    for i in ssn:
        if not i.isdigit():
            return False

        return True
        
    
main() # Call the main function
