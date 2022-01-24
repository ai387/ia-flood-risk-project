# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from math import sqrt
from utils import sorted_by_key # noqa
import station as st # importing the classes that are made in submodule
import stationdata
from stationdata import build_station_list # importing all data abt the stations
import datafetcher
from station import MonitoringStation

from haversine import haversine, Unit # importing haversine library to calculate distance of monitoringstation from coord

# stations = stationdata.build_station_list(True)
#p = (0, 0) # assume monitoring station is at the origin

#stations = stationdata.build_station_list(True)
#p = (52.2053, 0.1218)
'''
for j in stations:
    list_lines = str(j).splitlines()
    test = MonitoringStation.__init__(list_lines[0],list_lines[1],list_lines[2],list_lines[3],list_lines[4],list_lines[5],list_lines[6],list_lines[7])
print(test)

'''
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

    # using pythagoras to find distance (because haversine function had issues (see attempts below)
    distances_list = []
    for a, b in station_coord2:
        distance = sqrt((a-p[0]) ** 2 + (b-p[1]) ** 2)
        distances_list.append(distance)
    station_coord_tuples = list(zip(station_name, station_town, distances_list))  # making a list of tuples for each name and coord
    sorted = sorted_by_key(station_coord_tuples, 1, reverse=False)
    return sorted  # sorting tuple according to distance




# TASK 1C

def stations_within_radius(stations, centre, r):


'''
2.1.3. Task 1C: stations within radius

In the submodule geo implement a function that returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x. The required function signature is:

def stations_within_radius(stations, centre, r):
where stations is a list of MonitoringStation objects, centre is the coordinate x and r is the radius.
Demonstration program

Provide a program file Task1C.py that uses the function geo.stations_within_radius to build a list of stations within 10 km of the Cambridge city centre (coordinate (52.2053, 0.1218)). Print the names of the stations, listed in alphabetical order. Representative output:

['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']

'''






#print(stations_by_distance(stations, p))

#print(station_coord_tuples)
#import datafetcher
#from .station import MonitoringStation

#def stations_by_distance(stations, p):
#list_station = station.MonitoringStation.__repr__()
#print(list_station)

#stations = stationdata.build_station_list()

'''

distances = []
for coord in coords:
distance = haversine((0,0),coord,unit='km')

distances.append(distance)

#print(distances)
print(distance)
print(distances)
#station_coord.split(',') # splitting
'''