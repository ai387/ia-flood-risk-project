from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem import station


def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    output = stations_highest_rel_level(stations, N)
    for a, b in output:
        print(a, b)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
