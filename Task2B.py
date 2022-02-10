from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem import station

# GETTING NEGATIVE NUMBERS IN THE OUTPUT
# NEED TO CHANGE FORMATTING OF OUTPUT


def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    output = stations_level_over_threshold(stations, tol)
    print(output)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()