import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
from .analysis import polyfit

# Task 2E
'''Implement in a submodule plot a function that displays a plot (using Matplotlib) of the water level data against
time for a station, and include on the plot lines for the typical low and high levels. The axes should be labelled and
use the station name as the plot title. The function should have the signature:

def plot_water_levels(station, dates, levels):
where station is a MonitoringStation object.
'''
def plot_water_levels(station, dates, levels):
    # station --> one station (not iterating through the list of stations)

    #typ_low = station.typical_range[0]
    #typ_high = station.typical_range[1]

    # Plot
    plt.plot(dates, levels)
    #plt.plot(dates, typ_low)
    #plt.plot(dates, typ_high)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

# Task 2F

def plot_water_level_with_fit(station, dates, levels, p):
    dates_coord = []
    for each_date in dates:
        dates_float = matplotlib.dates.date2num(each_date)
        dates_coord.append(dates_float)
    x = dates_coord
    '''print(x)'''
    y = levels
    d0 = x[-1]
    p_coeff = np.polyfit(x - d0, y, p)
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = x
    plt.plot(x1, poly(x1 - d0))
    y_low, y_high = station.typical_range[0], station.typical_range[1]
    plt.plot(dates, y_low * np.ones(len(dates)))
    plt.plot(dates, y_high * np.ones(len(dates)))
    plt.legend(["Past level data", "Typical High", "Typical Low"])

    #Add the title, x and y labels, and rotate the xticks to make it show out clearly
    plt.title(station)
    plt.xlabel('date in floats')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)

    plt.tight_layout()
    # Display plot
    plt.show()