from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem import station
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
'''
Provide a program file Task2E.py that plots the water levels over the past 10 days for the 5 stations at which the
current relative water level is greatest.
'''
def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    output = stations_highest_rel_level(stations, 5) # 5 stations with greatest current relative water level
    for a, b in output:
        for each_station in stations:         # Find station
            if each_station.name == a:
                station_a = each_station
                dt = 10
                dates, levels = fetch_measure_levels(
                    station_a.measure_id, dt=timedelta(days=dt))
                plot_water_levels(a, dates, levels)


if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()
