
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run1():
    stations = build_station_list()
    print("There are ", len(rivers_with_station(stations)), " stations with at least one monitoring system.")
    output = rivers_with_station(stations)
    print("{}".format(output[:10]))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run1()
