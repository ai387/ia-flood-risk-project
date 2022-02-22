
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

'''
In a submodule analysis implement a function that given the water level time history (dates, levels) 
for a station computes a least-squares fit of a polynomial of degree p to water level data. The function 
should return a tuple of (i) the polynomial object and (ii) any shift of the time (date) axis (see below). 
The function should have the signature:

def polyfit(dates, levels, p):

Typical usage for a polynomial of degree 3 would be:
poly, d0 = polyfit(dates, levels, 3)
where poly is a numpy.poly1d object an d0 is any shift of the date (time) axis.
'''

# Task 2F
def polyfit(dates, levels, p):
    dates_coord = []
    for each_date in dates:
        dates_float = matplotlib.dates.date2num(each_date)
        dates_coord.append(dates_float)

    x = dates_coord
    y = levels
    d0 = x[-1]
    p_coeff = np.polyfit(x - d0, y, p)
    poly = np.poly1d(p_coeff)
    return poly, d0

    '''

    # Create set of 10 data points on interval (1000, 1002)
x = np.linspace(10000, 10002, 10)
y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43, 0.31, 0.01, -0.05]

# Using shifted x values, find coefficient of best-fit
# polynomial f(x) of degree 4
p_coeff = np.polyfit(x - x[0], y, 4)

# Convert coefficient into a polynomial that can be evaluated
# e.g. poly(0.3)
poly = np.poly1d(p_coeff)

# Plot original data points
plt.plot(x, y, '.')

# Plot polynomial fit at 30 points along interval (note that polynomial
# is evaluated using the shift x)
x1 = np.linspace(x[0], x[-1], 30)
plt.plot(x1, poly(x1 - x[0]))

# Display plot
plt.show()
    '''
