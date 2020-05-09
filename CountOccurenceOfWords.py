def main():
    # Prompt the user to enter a file
    filename = input('Enter a file: ').strip()
    infile = open(filename, 'r')

    wordCounts = {}  # Create an empty dictionary to count words
    for line in infile:
        processLine(line.lower(), wordCounts)

    pairs = list(wordCounts.items())  # Get pairs from the dictionary

    items = [[x,y] for (y,x) in pairs] # Reverse pairs in the list

    items.sort()  # sort pairs in the list

    for i in range(len(items) - 1, len(items) - 11, -1):
        print(items[i][1] + '\t' + str(items[i][0]))

# Count each word in the line
def processLine(line, wordCounts):
    line = replacePunctuations(line)  # Replace punctuations with space
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

# Replace punctuation in the line with space
def replacePunctuations(line):
    for ch in line:
        if ch in "!@#$%^&*()_+=`<>?,.;:{}[]|'\"":
            line.replace(ch, ' ')

    return line

main()
        
                                       
             
