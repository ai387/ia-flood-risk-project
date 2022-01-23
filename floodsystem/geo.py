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
list_items = []
station_name = []
station_coord = []


for each_station in list_of_stations:
    list_lines = str(each_station).splitlines() # splitting the data in a list, where each item = line
    counter=0
    for each_line in list_lines:
        counter += 1
        items = each_line.split(': ')
        items = items [1::2]
        for each_item in items:
            list_items.append(each_item)
            if counter == 1:
                station_name.append(each_item)
            if counter == 4:
                station_coord.append(each_item)


'''

        for item in items:
            
            list_items.append(item)
        list_items
        # splitting each line into its separate items
        counter = 0
        for item in items:
            counter += 1
            if counter == 1:
                station_name.append(item)
            elif counter == 4:
                station_coord.append(item)

print(station_name)

#print(list_lines, '\n', list_items)

'''

'''
names = []

for item in list_of_stations:
    counter = 0
    for i in item:
        counter += 1
        if counter == 1:
            names.append(item[counter])
        else: continue






station_id = stationdata
measure_id
label =
coord =
typical_range
river
town
st.MonitoringStation.__init__()
'''


#import datafetcher
#from .station import MonitoringStation

#def stations_by_distance(stations, p):
#list_station = station.MonitoringStation.__repr__()
#print(list_station)

#stations = stationdata.build_station_list()
