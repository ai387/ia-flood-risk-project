# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
        self.risk_level = None
        self.pred_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    # Task 1F
    def typical_range_consistent(self):
        if self.typical_range is None:  #This is to identify the terms with no data
            running = False
        else:
            if self.typical_range[0] > self.typical_range[1]: #This is to identify the terms with low range > high range
                running = False
            else:
                running = True

        return running

    # Task 2B
    def relative_water_level(self):
        if self.typical_range_consistent() is False or self.latest_level is None:
            # This is to identify the terms with no data
            # by using attributes self.latest_level ,
                # NB 'self.typical_range is None' has already been accomodated in previous function
            # and by using function self.typical_range_consistent()
            return None
        else:
            lat_lev = self.latest_level
            typ_rang_low = self.typical_range[0]
            typ_rang_high = self.typical_range[1]
            output = (lat_lev - typ_rang_low) / (typ_rang_high - typ_rang_low)
            # Returns the ratio of the actual level over the typical range
            return float(output)




# Task 1F
def inconsistent_typical_range_stations(stations):
    inconsistent_stations = []
    for each_station in stations:
        if MonitoringStation.typical_range_consistent(each_station) == False: # Pick up all the terms with False output
            inconsistent_stations.append(each_station.name)
    return inconsistent_stations

# Task 2G
def consistent_typical_range_stations(stations):
    """
    returns the stations that have consistent typical range data
    Inputs
    ------
    stations: list of MonitoringStation objects
    Returns
    ------
    a list of stations that have consistent typical range data
    """

    consistent_station_list = []
    for station in stations:
        if station.typical_range_consistent() == True:
            consistent_station_list.append(station)
    return consistent_station_list