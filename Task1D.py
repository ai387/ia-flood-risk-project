from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station

def run():
    stations = build_station_list()
    print(rivers_with_station(stations))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()