import datetime
from matplotlib.dates import date2num

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.station import consistent_typical_range_stations


def run():
    """Requirements for Task 2G
    Using your implementation, list the towns where you assess the risk of flooding to be greatest.
    Explain the criteria that you have used in making your assessment, and rate the risk at ‘severe’,
    ‘high’, ‘moderate’ or ‘low’."""

    stations = build_station_list()
    stations = consistent_typical_range_stations(stations)
    '''remove stations with invalid data or inconsistent data, return a list of consistent stations'''
    update_water_levels(stations)
    stations = stations[0:50]
    '''update latest data'''

    for station in stations:
        dt, p = 2, 4
        try:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            t = date2num(dates)
            poly, d0 = polyfit(dates, levels, p)
            tmr = datetime.date.today() + datetime.timedelta(days=1)
            '''finding the date for tomorrow'''
            tmr_num = date2num(tmr)
            '''floating the date of tomorrow'''
            pred_rel_water_level = poly(tmr_num - d0)
            '''print(pred_rel_water_level)'''
            '''To record the progress'''
            '''The following is to classify each station to different categories by current risk: '''
        except:
            station.risk_level = "Unknown"
            continue
        if pred_rel_water_level > 3:
            station.risk_level = "Severe"
            station.pred_level = pred_rel_water_level
        elif pred_rel_water_level > 1:
            station.risk_level = "High"
            station.pred_level = pred_rel_water_level
        elif pred_rel_water_level > 0:
            station.risk_level = "Moderate"
            station.pred_level = pred_rel_water_level
        else:
            station.risk_level = "Low"
            station.pred_level = pred_rel_water_level

    List_of_severe_risk = []
    pred_sev = []
    name_sev = []
    high_list = []
    pred_high = []
    name_high = []
    for each in stations:
        if each.risk_level == 'Severe':
            List_of_severe_risk.append(each.town)
            pred_sev.append(each.pred_level)
            name_sev.append(each.name)
        elif each.risk_level == 'High':
            high_list.append(each.town)
            pred_high.append(each.pred_level)
            name_high.append(each.name)
        else:
            pass
    '''List_of_severe_risk = list(dict.fromkeys(List_of_severe_risk))
    List_of_high_list = list(dict.fromkeys(high_list))'''
    SEVERE = list(zip(List_of_severe_risk, pred_sev, name_sev))
    HIGH = list(zip(high_list, pred_high, name_high))

    print('The towns are predicted to have SEVERE risk (Town, predicted level, Name): ')
    print(SEVERE)
    print('The towns are predicted to have HIGH risk (Town, predicted level, Name): ')
    print(HIGH)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()