def main():
    numbers = [eval(x) for x in input('Enter integers between 1 and 100: ').split()]
    counts = 100*[0]

    updatedCounts = countOccurrence(numbers, counts)
    displayOccurrence(updatedCounts)

def countOccurrence(numbers, counts):
    for number in numbers:
        counts[number - 1] += 1
    return counts

def displayOccurrence(counts):
    for number in range(1, len(counts) + 1):
        if counts[number - 1] != 0:
            print(str(number) + ' occurs ' + str(counts[number - 1]) + (' times' if counts[number - 1] > 1 else ' time'))

            
main()
