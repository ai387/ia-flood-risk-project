# ARZINA: RUNNING THIS CODE IN GEO GIVES YOU A DIFFERENT OUTPUT TO WHAT IS EXPECTED (ON THE TASK IT GIVES EXAMPLE OUTPUT,
# ARZINA: BUT MY OUTPUT IS NOT THE SAME'

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    stations = build_station_list()
    output = rivers_with_station(stations)
    print("There are ", len(output), " stations with at least one monitoring system.")
    print("{}".format(output[:10]))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
