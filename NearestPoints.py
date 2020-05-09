# Compute the distance between two points (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2

def nearestPoints(points):
    # P1 and p2 are the indexes in the points list
    p1, p2 = 0, 1

    shortestDistance = distance(points[p1][0], points[p1][1],
                                points[p2][0], points[p2][1])   # initialize shortestDistance

    # Compute the distance between every two points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i][0], points[i][1],
                                points[j][0], points[j][1]) # Find distance

            if shortestDistance > d:
                p1, p2 = i, j  # Update p1, p2
                shortestDistance = d  # New shortest distance

    return p1, p2

def main():
    numberOfPoints = eval(input('Enter the number of points: '))

    # Create a list to store the points
    points = []
    print('Enter',numberOfPoints,'Points',end = '')
    for i in range(numberOfPoints):
        point = 2 *[0]
        point[0], point[1] = eval(input('Enter coordinates separated by comma: '))
        points.append(point)

    # p1 and p2 are the indexes in the points list
    p1, p2 = nearestPoints(points)

    #Display result
    print('The closest two points are (' +
          str(points[p1][0]) + ',' + str(points[p1][1]) +') and (' +
          str(points[p2][0]) + ',' + str(points[p1][0]) + ')')

main()
                
            
