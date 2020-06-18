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
    print("%.5f" %integ) # Print calculated integral approximation (%.5f)

# Define the function
f = lambda x: (1/(1+x))

#Lets try out trapezoid rule with different steps size
# h = 0.5
trapezoid(f,0,1,0.5)
# Output => 0.55556
# h = 0.25
trapezoid(f,0,1,0.25)
# Output => 0.60762
# h = 0.125
trapezoid(f,0,1,0.125)
# Output => 0.64477
'''
The real value of the function is ln(2) or approximately 0.69315
As you can see smaller the steps the better is approximation
'''
