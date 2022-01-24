
# this code works fine in the submodule 'geo'
# however i get the error ' ModuleNotFoundError: No module named 'datafetcher' ' when i try to run it on here

# RUNNING THIS CODE IN GEO GIVES YOU A DIFFERENT OUTPUT TO WHAT IS EXPECTED (ON THE TASK IT GIVES EXAMPLE OUTPUT,
# BUT MY OUTPUT IS NOT THE SAME'
# I SUSPECT IT IS THE HAVERSINE FORMULA WHICH I'M USING WRONG

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

stations = build_station_list()

centre = (52.2053, 0.1218)
r = 10

print(stations_within_radius(stations, centre, r))
