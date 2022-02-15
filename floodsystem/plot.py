import matplotlib.pyplot as plt
from datetime import datetime, timedelta

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
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()