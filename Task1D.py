
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

#from floodsystem.geo import stations_of_river
# stations_of_river is a function we made in geo that finds all the stations belonging to a
# given 'river_name', which is in a given 'dictionary'


# writing a function that finds all the stations belonging to a given 'river_name', which is in a given 'dictionary'
# this is needed for the demonstration programme in 1D
def stations_of_river(dictionary, river_name):
    stations = dictionary[river_name]
    list_of_stations = []
    for each_station in stations:
        list_of_stations.append(each_station.name)
    return sorted(list_of_stations)



def run():
    stations = build_station_list()
    output1 = rivers_with_station(stations)
    print("There are ", len(output1), " stations with at least one monitoring system.")
    print("The first 10 rivers with at least one monitoring station:")
    print(output1[:10])

    output2 = stations_by_river(stations)
    print("Stations on the River Aire:")

    print(stations_of_river(output2, 'River Aire'))

    print("Stations on the River Cam:")

    print(stations_of_river(output2, 'River Cam'))

    print("Stations on the River Thames:")

    print(stations_of_river(output2, 'River Thames'))

  #  print(stations_by_river(stations))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
