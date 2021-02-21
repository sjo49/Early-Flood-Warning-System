from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import update_water_levels
import datetime

stations = build_station_list()
update_water_levels(stations)


def run():
    dt = 2
    p = 4
    current_high_stations = stations_highest_rel_level(stations, 5)
    # current_high_stations.remove(current_high_stations[0])
    for i in range(len(current_high_stations)):
        station_name = current_high_stations[i][0]
        s_index = [x for x, y in enumerate(stations) if y.name == station_name]
        ind = s_index[0]
        dates, levels = fetch_measure_levels(stations[ind].measure_id, dt=datetime.timedelta(days=dt))
        if len(dates) == 0 or len(levels) == 0:
            print(f'Dates and/or levels for {stations[ind].name} not returned properly from fetch_measure_levels (empty list returned)')
        else:
            plot_water_level_with_fit(stations[ind], dates, levels, p)


run() 

