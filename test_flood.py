from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem import station
from floodsystem.stationdata import build_station_list, update_water_levels
import numpy as np
from floodsystem.station import MonitoringStation

# Task 2B:
def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    output = stations_level_over_threshold(stations, tol)
    for each_outcome in output:
        assert each_outcome[1] > 0.8
        assert each_outcome[1] < 700  #Making sure the relative water level is within the required range
        assert type(each_outcome[0]) == str # Testing the name of water level is given

# Task 2C:
def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    output = stations_highest_rel_level(stations, N)
    assert len(output) == 10 # Testing the number of stations in the outcome matches the required number
    station_names = []
    for each in output:
        station_names.append(each[1])
    for station in stations:
        if station.name in station_names:
            assert output[1] == station.relative_water_level()
            # Assert whether the station name in the outcome match its relative water level
