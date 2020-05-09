def main():
    # Prompt the user to enter a genome
    genome = input('Enter a genome string: ').strip().upper()

    remainingLength = len(genome)
    start = isSubstring(genome, 'ATG')
    if start != -1:
        end = isSubstring
        


def isSubstring(first, second):
    remainingLength = len(first)
    startingIndex = 0;

    while len(second) <= remainingLength:
        if second != first[startingIndex : startingIndex + len(first)]:
            startingIndex += 1
            remainingLength -= 1
        else:
            return startingIndex

    return -1
