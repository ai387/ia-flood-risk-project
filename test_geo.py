
from math import sqrt
from tokenize import Number
from floodsystem.utils import sorted_by_key # noqa
from floodsystem.station import MonitoringStation # importing the classes that are made in submodule
from floodsystem.stationdata import build_station_list # importing all data abt the stations
from floodsystem.geo import stations_by_distance

from haversine import haversine, Unit

def test_stations_by_distance():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    distance_list = []
    station_list = stations_by_distance(stations, p)
    for each_station in station_list:
        distance_list.append(each_station[2])

    for each_term in stations:
        assert haversine(p, each_term.coord, unit='km') in distance_list