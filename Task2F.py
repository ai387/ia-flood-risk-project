
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem import station
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit

def run():
    stations = build_station_list()
    update_water_levels(stations)
    data = stations_highest_rel_level(stations, N=5)
    '''find the five stations at which the current relative water level is greatest'''
    stations_plot = []
    for each_tuple in data:
        stations_plot.append(each_tuple[0])
        '''build a list of five names of the stations'''
    for each_station in stations_plot:
        for station in stations:
            if station.name in [each_station]:
                id = station.measure_id
                print(station.name)
                '''find the corresponding measure_id for the five stations and plot its graph'''
                dt = 2
                dates, levels = fetch_measure_levels(id, dt=datetime.timedelta(days=dt))
                '''new = []
                for each_date in dates:
                    new_coord = matplotlib.dates.date2num(each_date)
                    new.append(new_coord)
                print(new)'''
                plot_water_level_with_fit(each_station, dates, levels, p=4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()