# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from utils import sorted_by_key # noqa
import station as st # importing the classes that are made in submodule
import stationdata # importing all data abt the stations

from haversine import haversine, Unit # importing haversine library to calculate distance of monitoringstation from coord

monitoring_station = ()
list_of_stations = stationdata.build_station_list(True)
#print(list_of_stations[0])
station_name = []
station_coord = []
station_town = []

for each_station in list_of_stations:
    list_lines = str(each_station).splitlines() # splitting data in a list, each component = each line of station info
    counter=0 # initialising counter to count each line of station info
    for each_line in list_lines:
        counter += 1 # adding one to counter for each line of station info e.g. 1 is Station name, 2 is id etc...
        items = each_line.split(': ') # splitting each line into a list (e.g. [Station name, Bourton Dickler])
        items = items [1::2] # removing list descriptor e.g. removing Station name
        if counter == 1: # if the item is the first in the list it is a station name
            items = str(items)[6:-2] # getting rid of white spaces etc
            station_name.append(items)
        if counter == 4: # if the item is the fourth in the list it is the station coordinates
            items = str(items)[5:-2] # getting rid of white spaces etc
            station_coord.append(items)
        if counter == 5: # if the item is the fifth in the list it is the town name
            items = str(items)[11:-2] # getting rid of white spaces etc
            station_town.append(items)

'''
station_coord2 = []
for i in station_coord:
    clean_coord = str(i)[5:-2] # list of coordinates without white spaces
    station_coord2.append(clean_coord)
'''
print(station_name)
print(station_coord)
print(station_town)
#station_coord.split(',') # splitting

#station_coord_tuples = list(zip(station_name, station_coord2)) # making a list of tuples for each name and coord

#print(station_coord_tuples)
#import datafetcher
#from .station import MonitoringStation

#def stations_by_distance(stations, p):
#list_station = station.MonitoringStation.__repr__()
#print(list_station)

#stations = stationdata.build_station_list()
