# ARZINA: RUNNING THIS CODE IN GEO GIVES YOU A DIFFERENT OUTPUT TO WHAT IS EXPECTED (ON THE TASK IT GIVES EXAMPLE OUTPUT,
# ARZINA: BUT MY OUTPUT IS NOT THE SAME'
# ARZINA: I SUSPECT IT IS THE HAVERSINE FORMULA WHICH I'M USING WRONG

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    print(stations_within_radius(stations, centre, r))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()