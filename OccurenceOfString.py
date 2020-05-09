def main():
    first = input("Enter the first string: ").strip()
    second = input("Enter the second string: ").strip()
   
    print('The number of occurence of {0} in "{1}" is'.format(second, first),\
          numberOfOccurences(first, second))
          
  
# Check if the first string is a substring of the second string
def numberOfOccurences(first, second):
    remainingLength = len(first)
    startingIndex = 0;
    indexes = []

    while len(second) <= remainingLength:
        if second != first[startingIndex : startingIndex + len(second)]:
            startingIndex += 1
            remainingLength -= 1
        else:
            indexes.append(startingIndex)
            startingIndex += len(second)
            remainingLength -= len(second)
              

    return len(indexes)

        
    
main()
