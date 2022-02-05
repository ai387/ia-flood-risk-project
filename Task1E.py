# i get an incorrect output for 1E (it's mostly there but if you run it, you will see that some stations = 0,
# and we want to remove these from the output, but idk how)


'''
Demonstration program

Provide a program file Task1E.py that prints the list of (river, number stations) tuples when N = 9.
Representative result is:

[('Thames', 55), ('River Great Ouse', 31), ('River Avon', 30), ('River Calder', 24), ('River Aire', 21),
('River Severn', 20), ('River Derwent', 18), ('River Stour', 16), ('River Wharfe', 14), ('River Trent', 14),
('Witham', 14)]
The above list has more then 9 entries since a number of rivers have 14 stations.
'''

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    stations = build_station_list()
    output = rivers_by_station_number(stations, 9)
    print(output)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()


from floodsystem import stationdata
