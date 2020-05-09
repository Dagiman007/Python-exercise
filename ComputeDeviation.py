from math import sqrt

def main():
    x = [eval(x) for x in input('Enter number: ').split()]
    print('The mean is', format(mean(x), '.2f'))
    print('The deviation is', format(deviation(x), '.2f'))

def deviation(x):
    meanX = mean(x)
    sum = 0
    for i in range(len(x)):
        sum += ((x[i] - meanX)**2) / (len(x) - 1)

    return sqrt(sum)

def mean(x):
    return sum(x) / len(x)
        
    
main()
