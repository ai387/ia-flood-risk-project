from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem import stationdata

'''
Demonstration program

Provide a program file Task1E.py that prints the list of (river, number stations) tuples when N = 9.
Representative result is:

[('Thames', 55), ('River Great Ouse', 31), ('River Avon', 30), ('River Calder', 24), ('River Aire', 21),
('River Severn', 20), ('River Derwent', 18), ('River Stour', 16), ('River Wharfe', 14), ('River Trent', 14),
('Witham', 14)]
The above list has more then 9 entries since a number of rivers have 14 stations.
'''

def run():
    stations = build_station_list()
    N = 9
    output = rivers_by_station_number(stations, N)
    print(output)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()



