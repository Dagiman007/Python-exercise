'''Assume a circle of radius 1 is inscribed in a square \
with area 4. The probability that a point in a square falls
in the circle is pi/4(circleArea/squareArea).
'''
import random

NUBMER_OF_TRIALS = 1000000 #constant
numberOfHits = 0

for i in range(NUBMER_OF_TRIALS):
    x = random.random()*2 - 1
    y = random.random()*2 - 1

    if x**2 + y**2 <= 1:
        numberOfHits += 1
pi = (4 * numberOfHits)/NUBMER_OF_TRIALS
print("Pi is ",pi)
