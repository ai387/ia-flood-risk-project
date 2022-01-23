# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from utils import sorted_by_key # noqa
import station as st # importing the classes that are made in submodule
import stationdata # importing all data abt the stations


list_of_stations = stationdata.build_station_list(True)
#print(list_of_stations[0])
station_name = []
station_coord = []

for each_station in list_of_stations:
    list_lines = str(each_station).splitlines() # splitting data in a list, each component = each line of station info
    counter=0 # initialising counter to count each line of station info
    for each_line in list_lines:
        counter += 1 # adding one to counter for each line of station info e.g. 1 is Station name, 2 is id etc...
        items = each_line.split(': ') # splitting each line into a list (e.g. [Station name, Bourton Dickler])
        items = items [1::2] # removing list descriptor e.g. removing Station name
        if counter == 1: # if the item is the first in the list it is a station name
            station_name.append(items)
        if counter == 4: # if the item is the fourth in the list it is the station coordinates
            station_coord.append(items)

#import datafetcher
#from .station import MonitoringStation

#def stations_by_distance(stations, p):
#list_station = station.MonitoringStation.__repr__()
#print(list_station)

#stations = stationdata.build_station_list()
