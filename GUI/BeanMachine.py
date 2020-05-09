import random

def main():
    numberOfBalls = eval(input('Enter the number of balls to drop: '))
    numberOfSlots = eval(input('Enter the number of slots in the bean machine: '))

    slots = [0] * numberOfSlots
    getSlots(numberOfBalls, slots)
    display(slots)

def getSlots(numberOfBalls, slots):
    while numberOfBalls > 0:
        path = ''
        for i in range(len(slots)):
            r = random.randint(0,1)
            if r == 0:
                path = path + 'L'
            else:
                path = path + 'R'

        # Count number of Rs
        count = 0
        for char in path:
            if char == 'R':
                count += 1

        print(path)
        slots[count - 1] += 1
        numberOfBalls -= 1

def display(slots):
    m = max(slots)
    for v in reversed(range(1, m + 1)):
        print(''.join('0' if x >= v else ' ' for x in slots))
    
    

    
main()        
