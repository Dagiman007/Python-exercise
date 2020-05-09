import cmath
import math

x = 1.0
y = 1.0
a = math.inf
b = math.nan

z = complex(x, y)
w = complex(x, a)
v = complex(x, b)

# Check if both numbers are finite
if cmath.isfinite(z):
    print('Complex number is finite')
else:
    print('Complex number is infinite')

if cmath.isinf(w):
    print('Complex number is infinite')
else: print('Complex number is finite')

if cmath.isnan(v):
    print('Complex number is NaN')
else: print('Complex number is not NaN')
