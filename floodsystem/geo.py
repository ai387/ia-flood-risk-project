# Copyright (C) 2018 Garth N. Wells
#
#SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from math import sqrt
from .utils import sorted_by_key # noqa
from .station import MonitoringStation # importing the classes that are made in submodule
from .stationdata import build_station_list # importing all data abt the stations

from haversine import haversine, Unit # importing haversine library to calculate distance of monitoringstation from coord

# stations = stationdata.build_station_list(True)
#p = (0, 0) # assume monitoring station is at the origin
#stations = stationdata.build_station_list(True)
#p = (52.2053, 0.1218)

#print(stations_by_distance(stations, p))

#print(station_coord_tuples)
#import datafetcher
#from .station import MonitoringStation

#def stations_by_distance(stations, p):
#list_station = station.MonitoringStation.__repr__()
#print(list_station)

#stations = stationdata.build_station_list()




# TASK 1B
def stations_by_distance(stations, p):
    station_name = []
    station_coord = []
    station_town = []
    for each_station in stations:
        list_lines = str(each_station).splitlines()  # splitting data in a list, each component = each line of station info
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

    # turning coordinates from string in list into tuples with float numbers
    station_coord2 = []
    for i in station_coord:
        i = i.strip('()')
        i = i.split(',')
        c = tuple(float(x) for x in i)
        station_coord2.append(c)

    # using haversine function to find distance (using unit = km)
    distances_list = []
    for coord in station_coord2:
        distance = haversine(p, coord, unit='km')
        distances_list.append(distance)
    station_coord_tuples = list(zip(station_name, station_town, distances_list))  # making a list of tuples for each name and coord
    sorted = sorted_by_key(station_coord_tuples, 1, reverse=False)
    return sorted  # sorting tuple according to distance







# TASK 1C
def stations_within_radius(stations, centre, r):
    station_name = []
    station_coord = []
    for each_station in stations:
        list_lines = str(
            each_station).splitlines()  # splitting data in a list, each component = each line of station info
        counter = 0  # initialising counter to count each line of station info
        for each_line in list_lines:
            counter += 1  # adding one to counter for each line of station info e.g. 1 is Station name, 2 is id etc...
            items = each_line.split(': ')  # splitting each line into a list (e.g. [Station name, Bourton Dickler])
            items = items[1::2]  # removing list descriptor e.g. removing Station name
            if counter == 1:  # if the item is the first in the list it is a station name
                items = str(items)[6:-2]  # getting rid of white spaces etc
                station_name.append(items)
            if counter == 4:  # if the item is the fourth in the list it is the station coordinates
                items = str(items)[5:-2]  # getting rid of white spaces etc
                station_coord.append(items)

    # turning coordinates from string in list into tuples with float numbers
    station_coord2 = []
    for i in station_coord:
        i = i.strip('()')
        i = i.split(',')
        c = tuple(float(x) for x in i)
        station_coord2.append(c)

    #using haversine function to find distance between centre and coord (using unit = km)
    counter = 0
    for coord in station_coord2:
        distance = haversine(centre, coord, unit='km')
        if distance > r:
            station_name.pop(counter)
        counter =+ 1
    sorted_station_name = sorted(station_name) # sorting list alphabetically
    return sorted_station_name

# Task 1D

def rivers_with_station(station):
    station_names = set()




