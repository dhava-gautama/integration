import numpy as np

# Trapezoid Rule #
'''
The trapezoid rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/2) \sum_{k=1}^N (f(x_k) + f(x_{k-1}))
    where x_k = a + k*dx and dx = (b - a)/N
Parameters
f    : function
a,b  : interval (a,b)
step : subsinterval size between (a,b)
'''
def trapezoid(f,a,b,step):
    x = np.arange(a,b+step,step) # Create array List of point between (a,b)
    n = len(x) # Returns the number of items in x array
    dx = (b-a)/n # Find value of dx
    sum = f(x[0]) # First value of sumation series
    for datapoint in range(1,n): # Add the rest value of sumation series
        sum += 2*f(x[datapoint])
    integ = (dx/2)*sum # Calculate the integral approximaiton
    print(integ)

f = lambda x: (np.sin(x))

trapezoid(f,0,1,0.001)
