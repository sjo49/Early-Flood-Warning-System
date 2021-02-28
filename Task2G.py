from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.stationdata import update_water_levels
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from floodsystem.flood import stations_level_over_threshold
stations = build_station_list()
update_water_levels(stations)


def run():
    dt = 2
    risk_station_list = stations_level_over_threshold(stations, 1)
    moderate_risk = []
    high_risk = []
    severe_risk = []
    for station_tuple in risk_station_list:
        station_name = station_tuple[0]
        s_index = [x for x, y in enumerate(stations) if y.name == station_name]
        ind = s_index[0]
        dates, levels = fetch_measure_levels(stations[ind].measure_id, dt=datetime.timedelta(days=dt))
        levels_array = True
        for i in range(len(levels)):
            if type(levels[i]) != float:
                levels_array = False
        if levels_array == False:
            pass
        else:
            days = np.zeros(len(dates))
            level_array = np.zeros(len(levels))
            for i in range(len(dates)):
                days[i] += float(dates[i].day)
            for i in range(len(levels)):
                level_array[i] += float(levels[i])
            slope, intercept = np.polyfit(days, level_array, 1)
            if station_tuple[1] > 10 or (station_tuple[1] > 8 and slope >= 0):
                severe_risk.append(station_tuple[0])
            elif station_tuple[1] > 5 and slope >= -0.5:
                high_risk.append(station_tuple[0])
            elif (station_tuple[1] > 2 and slope >= 0) or station_tuple[1] >= 5:
                moderate_risk.append(station_tuple[0])
    if len(severe_risk) != 0:
        print('Severe risk towns: {0}.'.format(severe_risk))
    else:
        print('No severe risk towns.')
    if len(high_risk) != 0:
        print('High risk towns: {0}.'.format(high_risk))
    else:
        print('No high risk towns.')
    if len(moderate_risk) != 0:
        print('Moderate risk towns: {0}.'.format(moderate_risk))
    else:
        print('No moderate risk towns.')


run()
