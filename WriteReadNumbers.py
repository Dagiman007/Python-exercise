from random import randint

def main():
    # Open file for writing data
    outfile = open(r'C:\Users\DagiMan\Desktop\Python Programming - CBT Nuggets\Exercise\Numbers.txt', 'w')
    for i in range(10):
        outfile.write(str(randint(0,9)) + ' ')
    outfile.close()

    # Open file for reading data
    infile = open(r'C:\Users\DagiMan\Desktop\Python Programming - CBT Nuggets\Exercise\Numbers.txt', 'r')
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    for number in numbers:
        print(number, end = ' ')
    infile.close()

main()
        
    
        
        
