import pickle

def main():
    # Open file for writing binary
    outfile = open(r'C:\Users\DagiMan\Desktop\Python Programming - CBT Nuggets\Exercise\pickle.dat', 'wb')
    pickle.dump(45, outfile)
    pickle.dump(56.6, outfile)
    pickle.dump('Programming is really fun', outfile)
    pickle.dump([x**2 for x in range(4)], outfile)
    outfile.close() # Close the output file

    # Open file for reading binary
    infile = open(r'C:\Users\DagiMan\Desktop\Python Programming - CBT Nuggets\Exercise\pickle.dat', 'rb')
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    infile.close()

   
main()
