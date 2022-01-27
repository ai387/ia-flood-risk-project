# when running task 1A and 1B I get the error ModuleNotFoundError: No module named 'datafetcher'
# lmk if u get this error too
# this code works fine in the submodule geo, but not after importing it on here

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
#import stationdata
#stations = stationdata.build_station_list(True)
def run():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    print(stations_by_distance(stations, p))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()


# NEED TO CHANGE CODE SO THAT IT ONLY PRINTS 10 CLOSEST AND 10 FURTHEST