from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem import station


def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    output = stations_level_over_threshold(stations, tol)
    for a, b in output:
        print(a, b)  # iterating through list so that each tuple is printed on a new line

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()