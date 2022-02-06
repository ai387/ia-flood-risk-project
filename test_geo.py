
from math import sqrt
from tokenize import Number
from floodsystem.utils import sorted_by_key # noqa
from floodsystem.station import MonitoringStation # importing the classes that are made in submodule
from floodsystem.stationdata import build_station_list # importing all data abt the stations

from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

from haversine import haversine, Unit


# Task 1B
def test_stations_by_distance():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    distance_list = []
    station_list = stations_by_distance(stations, p)
    for each_station in station_list:
        distance_list.append(each_station[2])

    for each_term in stations:
        assert haversine(p, each_term.coord, unit='km') in distance_list

# Task 1C
def test_stations_within_radius():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    name_list = stations_within_radius(stations, centre, r)
    for station in stations:
        if station.name in name_list:
            assert haversine(centre, station.coord, unit='km') - r < 0

# Task 1D
def test_rivers_with_station():
    stations = build_station_list()
    river_station_list = rivers_with_station(stations)
    for each_station in stations:
        assert each_station.river in river_station_list
    assert len(river_station_list) == len(list(set(river_station_list)))


def test_stations_by_river():
    stations = build_station_list()
    assert type(stations_by_river(stations)) is dict


# Task 1E
def test_rivers_by_station_number():
    stations = build_station_list()
    N = 9
    output = rivers_by_station_number(stations, N)
    assert len(output) < 100
    assert type(output) is list


# Task 1F

'''
def run():
    stations = build_station_list()
    output = inconsistent_typical_range_stations(stations)
    output = sorted(output)
    print(output)
'''
