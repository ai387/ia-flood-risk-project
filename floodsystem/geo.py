# Copyright (C) 2018 Garth N. Wells
#
#SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from math import sqrt
from tokenize import Number
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
    distances_list = []

    for each_station in stations:
        station_name.append(each_station.name)
        station_coord.append(each_station.coord)
        station_town.append(each_station.town)

    # using haversine function to find distance (using unit = km)
    for coord in station_coord:
        distance = haversine(p, coord, unit='km')
        distances_list.append(distance)
    station_coord_tuples = list(
        zip(station_name, station_town, distances_list))  # making a list of tuples for each name and coord
    sorted = sorted_by_key(station_coord_tuples, 2,
                           reverse=False)  # the distance is the third entry in the tuple, therefore, the number entried should be '2' instead of '1'

    return sorted  # sorting tuple according to distance

    '''        
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
    '''



# TASK 1C
'''
In the submodule geo implement a function that returns a list of all stations (type MonitoringStation) within 
radius r of a geographic coordinate x. The required function signature is:
def stations_within_radius(stations, centre, r):
where stations is a list of MonitoringStation objects, centre is the coordinate x and r is the radius.
'''
def stations_within_radius(stations, centre, r):
    station_list = stations_by_distance(stations, centre)
    # make a list of stations with the distance to centre by using 1B function
    within_radius_list = []
    for station in station_list:
        if station[2] < r:
            within_radius_list.append(station[0])
            # add the station with the distance < r to the new list
        else:
            pass
            # pass all the other stations
    return sorted(within_radius_list)

    '''
        station_name = []
    station_coord = []
    for each_station in stations:
        station_name.append(each_station.name)
        station_coord.append(each_station.coord)

    # using haversine function to find distance between centre and coord (using unit = km)
    Num = 0
    station_list = []
    for coord in station_coord:
        distance = haversine(centre, coord, unit='km')
        if distance < r:
            # station_name.pop(counter)
            station_list.append(station_name[Num])
            Num += 1
    sorted_station_name = sorted(station_list)  # sorting list alphabetically
    return sorted_station_name
    '''

    '''
    for each_station in stations:
        list_lines = str(each_station).splitlines()  # splitting data in a list, each component = each line of station info
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
    '''


# Task 1D

'''
In the submodule geo develop a function that, given a list of station objects, returns a container (list/tuple/set) 
with the names of the rivers with a monitoring station. The function should have the signature:
def rivers_with_station(stations):
where stations is a list of MonitoringStation objects. The returned container should not contain duplicate entries.
Tip
Consider returning a Python set object. A set contains only unique elements. This is useful for building a collection 
of river names since a set will never contain duplicate entries, no matter how many times a river name is added. A 
brief example of using a set is available here.


In the submodule geo implement a function that returns a Python dict (dictionary) that maps river names (the ???key???) to 
a list of station objects on a given river. The function should have the signature:
def stations_by_river(stations):
where stations is a list of MonitoringStation objects.
'''

def rivers_with_station(stations):
    river_with_station_list = []
    for each_station in stations:
        river_name = each_station.river # finding name of river from station

    # the 'not in' function checks whether the specified river_name is an element of the list
        if river_name not in river_with_station_list:
            river_with_station_list.append(river_name)

    return sorted(river_with_station_list)

def stations_by_river(stations):
    dictionary = {} # creating empty dictionary
    # station_names = []
    for each_station in stations:
        river_name = each_station.river
        if each_station.river not in dictionary.keys(): # e.g. 'Burton Dikler' caused an error so if the element is
            # empty, we state it to be [] in the dictionary
            dictionary[each_station.river] = []
        #station_names.append(each_station.name)
        #dictionary[river_name] = station_names # adding term to dictionary
        #dictionary[river_name].append(station_name)  # adding term to key
        dictionary[river_name].append(each_station) # adding term to dictionary
    return dictionary




# Task 1E
    '''
    Implement a function in geo that determines the N rivers with the greatest number of monitoring stations. It should
    return a list of (river name, number of stations) tuples, sorted by the number of stations. In the case that there are
    more rivers with the same number of stations as the N th entry, include these rivers in the list. The function should
    have the signature:

    def rivers_by_station_number(stations, N):
    where stations is a list of MonitoringStation objects.
    '''

# have lists
# sort by increasing num of stations
# zip it into tuples


def rivers_by_station_number(stations, N):
    # dictionary = {}
    # reusing the function from task 1D ??? making alphabetical list of rivers which have a station
    list_of_rivers = rivers_with_station(stations)
    num_stations = [0] * len(list_of_rivers)

    index = 0
    new_river_list = []
    new_station_count = []
    for each_river in list_of_rivers:
        # dictionary[each_river] = 0 # at the start of function, assuming each river has 0 stations
    # in the rest of the function we iterate through list of stations and +1 for each station that a river has
        num = 0
        for each_station in stations:
            if each_station.river == each_river:
                num += 1
        num_stations[index] = num

        if num > (N-1):
            new_river_list.append(each_river)
            new_station_count.append(num)
            # add all rivers with the number greater than N into a new list

        index += 1

# ERROR CHECK - write error if no.stations ends up being too large

    river_station_tuples = list(
        zip(new_river_list, new_station_count))  # making a list of tuples for each river and number of stations
    sorted = sorted_by_key(river_station_tuples, 1, reverse=True)

    return sorted
