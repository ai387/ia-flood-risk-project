from math import sqrt
from tokenize import Number
from .utils import sorted_by_key # noqa
from .station import MonitoringStation # importing the classes that are made in submodule
from .stationdata import build_station_list # importing all data abt the stations




# Task 2B part 2

'''
In the submodule flood, implement a function that returns a list of tuples, where each tuple holds 
(i) a station (object) at which the latest relative water level is over tol and 
(ii) the relative water level at the station. 
The returned list should be sorted by the relative level in descending order. 
The function should have the signature: def stations_level_over_threshold(stations, tol):
where stations is a list of MonitoringStation objects. 
Consider only stations with consistent typical low/high data.

'''

def stations_level_over_threshold(stations, tol):
    station_names = []
    relative_water_level_above_tol = []
    for each_station in stations:
        if typical_range_consistent(each_station) == True:
            water_level = relative_water_level(each_station)
            if water_level > tol:
                station_names.append(each_station.name)
                relative_water_level_above_tol.append(water_level)
            else:
                continue
        else:
            continue
    station_level_tuples = list(
        zip(station_names, relative_water_level_above_tol))  # making a list of tuples for each name and level
    sorted = sorted_by_key(station_level_tuples, 1,
                           reverse=True)  # water level is the 2nd entry in the tuple, therefore, the number entred 2
    return sorted