
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations




def run():
    stations = build_station_list()
    output = inconsistent_typical_range_stations(stations)
    output = sorted(output)
    print(output)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
