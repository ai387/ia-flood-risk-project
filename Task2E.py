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
        # Station name to find
        station_name = a

        # Find station
        station_a = None
        for each_station in stations:
            if each_station.name == station_name:
                station_a = each_station
                dt = 10
                dates, levels = fetch_measure_levels(
                    station_a.measure_id, dt=timedelta(days=dt))
                plot_water_levels(station, dates, levels)

'''    

    for station_t in top_stations:
        station = station_t[0]
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=10))
        plot_water_levels(station, dates, levels)
'''
'''
    # Check that station could be found. Return if not found.
    if not station_cam:
        print("Station {} could not be found".format(station_name))
        return
'''
    # Alternative find station 'Cam' using the Python 'next' function
    # (https://docs.python.org/3/library/functions.html#next). Raises
    # an exception if station is not found.
    # try:
    #     station_cam = next(s for s in stations if s.name == station_name)
    # except StopIteration:
    #     print("Station {} could not be found".format(station_name))
    #     return

    # Fetch data over past 2 days
    #dt = 5
    #dates, levels = fetch_measure_levels(
    #    station_a.measure_id, dt=datetime.timedelta(days=dt))

    # Print level history
   # for date, level in zip(dates, levels):
    #    print(date, level)


if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()
