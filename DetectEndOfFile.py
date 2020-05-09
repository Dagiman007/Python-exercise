import pickle

def main():
    # Open file for writing binary
    outfile = open(r'C:\Users\DagiMan\Desktop\Python Programming - CBT Nuggets\Exercise\numbers.dat', 'wb')

    data = eval(input('Enter an integer (the input exits ' +
                      ' if the input is 0: '))
    
    while data != 0:
        pickle.dump(data, outfile)
        data = eval(input('Enter an integer (the input exits ' +
                      ' if the input is 0: '))

    outfile.close()

    # Open file for reading
    infile = open(r'C:\Users\DagiMan\Desktop\Python Programming - CBT Nuggets\Exercise\numbers.dat', 'rb')

    end_of_file = False
    while not end_of_file:
        try:
            print(pickle.load(infile), end = ' ')
        except EOFError:
            end_of_file = True

    infile.close()

    print('\nAll objects are read')

main()
        
