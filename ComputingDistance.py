''' A program that computes the distance between
    two coordinate points in a plane '''

#get the points from the user

x1,y1 = eval(input("Please enter the first points, the coordinates separated by comma :"))
x2,y2 = eval(input("Enter the second points, the coordinates separated by comma :"))

#compute the distance between the two points

def distanceFunc(x,y) :
    return (x**2 + y**2)**0.5
     

distance = distanceFunc(x2-x1,y2-y1)

print("The distace between (",x1,',',y1,") and (",x2,',',y2,") is ",distance)
