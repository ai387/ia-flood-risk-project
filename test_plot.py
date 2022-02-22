from floodsystem.plot import plot_water_levels


# Task 2E:
def test_plot_water_levels():
    stations = build_station_list()
    update_water_levels(stations)
    output = stations_highest_rel_level(stations, 5) '''find 5 stations with greater rel_level'''
    for each in output:

        plot_water_levels(station, dates, levels)