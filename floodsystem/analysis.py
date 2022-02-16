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