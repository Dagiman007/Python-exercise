#This is the superclass
class Car(object):
    '''Class docstring'''
    def __init__(self,year,make,model):
        self.year = str(year)
        self.make = make
        self.model = model
        self.static = 'constant car data'
    def __str__(self):
        '''Formats  a string'''
        return 'String representation: {0} {1} {2}'.format(self.year,self.make,self.model)
    def printCar(self):
        '''Echoes back  the full name of the vehicle.'''
        print('{0} {1} {2}'.format(self.year,self.make,self.model))
        print(self.static)

ns = Car('1990','Nissan','Sentra')
str(ns)

print(ns)
print(ns.static)
ns.printCar()

#This is the subclass; inherits from car
class Motorcycle(Car):
    pass

hs = Motorcycle('2008','Honda','Shadow')

hs.printCar()
