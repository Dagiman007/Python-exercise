n = eval(input("Enter the number of asterisk: "))
asterisk = True
blankspace = False
asteriskNumber = 0

for line in range(-1, n):
    for j in range(n - line):
        print(" ", end = '')

    while asteriskNumber < line:
        if asterisk:
            asteriskNumber += 1
            print("*", end = '')
            asterisk = False
            blankspace = True
        elif blankspace:
            print(" ", end = '')
            asterisk = True
            blankspace = False
    print('')
    asterisk = True
    asteriskNumber = 0 
    
