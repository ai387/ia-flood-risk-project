# I have worked it out to solve importing error:
# Change the all importings from floodsystem to <from .(module) import (function/data)>
# add the <def run> and <if __name__> bits in the demo section

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
#import stationdata
#stations = stationdata.build_station_list(True)

def run():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    output = stations_by_distance(stations, p)
    #print(output)
    print("The 10 cloest stations from Cambridge: {}".format(output[:10]))
    print("The 10 furthest stations from Cambridge: {}".format(output[-10:]))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()


# I have added the code for only presenting 10 cloest and furthest stations