from math import sin, cos, tan, pi

def map_functions(x, functions):
    ''' map an iterable of functions on the object x '''

    res = []
    for func in functions:
        res.append(func(x))

    return res

familyOfFunctions = (sin, cos, tan)

print(map_functions(pi, familyOfFunctions))

def mapFunctions(x, functions):
    return [func(x) for func in functions]


