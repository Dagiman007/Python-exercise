from collections import Counter

def main():
    str1 = input('Enter the first string: ').strip()
    str2 = input('Enter the second string: ').strip()

    print('Are {0} and {1} anagrams?'.format(str1, str2), isAnagram(str1, str2))

def isAnagram(str1, str2):
    return Counter(str1) == Counter(str2)


main()
    
