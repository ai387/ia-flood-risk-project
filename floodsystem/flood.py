from math import sqrt
from tokenize import Number
from .utils import sorted_by_key # noqa
from .station import MonitoringStation  # importing the classes that are made in submodule
from .stationdata import build_station_list # importing all data abt the stations



# TASK 2B part 2
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
        if each_station.relative_water_level() is None:
            continue
        if each_station.typical_range_consistent() is True and each_station.relative_water_level() < 100:  # sanity check lol
            rel_water_level = each_station.relative_water_level()
            if rel_water_level > tol:
                station_names.append(each_station.name)
                relative_water_level_above_tol.append(rel_water_level)
            else:
                continue
        else:
            continue
    station_level_tuples = list(
        zip(station_names, relative_water_level_above_tol))  # making a list of tuples for each name and level
    sorted_list = sorted_by_key(station_level_tuples, 1, reverse=True)
    # water level is the 2nd entry in the tuple, therefore, the number entered 2
    return sorted_list



#Task 2C
'''
Implement a function in the submodule flood that returns a list of the N stations (objects) at which the water level, 
relative to the typical range, is highest. The list should be sorted in descending order by relative level. 

- find relative water level for each station
- output the station and water level
- sort the list highest to lowest
- print out the first N terms of the list
'''
def stations_highest_rel_level(stations, N):
    wat_lev_list = []
    for each_station in stations:
        if each_station.relative_water_level() is None:
            continue  # if data doesn't exist
        if each_station.typical_range_consistent() is True and each_station.relative_water_level() < 100:  # sanity check lol
            rel_water_level = each_station.relative_water_level()

            station_name = each_station.name
            wat_lev_list.append((station_name, rel_water_level))  # making a list of tuples
        output = sorted_by_key(wat_lev_list, 1, reverse=True)  # sorting list in descending order
    return output[:N]  # returning the first N terms
