from .flood import stations_level_over_threshold
import datetime
import numpy as np
from .datafetcher import fetch_measure_levels


def risk_level(stations, dt):
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
        if levels_array is False:
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
    return severe_risk, high_risk, moderate_risk
