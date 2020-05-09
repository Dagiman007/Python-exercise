def main():
    # Open file for output
    outfile = open(r'C:\Users\DagiMan\Desktop\Python Programming - CBT Nuggets\Exercise\Presidents.txt', 'w')

    # Write data to the file
    outfile.write('Bill Clinton\n')
    outfile.write('George Bush\n')
    outfile.write('Barack Obama')

    outfile.close()

main()
