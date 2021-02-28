from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import update_water_levels
import datetime

stations = build_station_list()
update_water_levels(stations)


def run():
    current_high_stations = stations_highest_rel_level(stations, 5)
    dt = 10
    for i in range(len(current_high_stations)):
        station_name = current_high_stations[i][0]
        s_index = [x for x, y in enumerate(stations) if y.name == station_name]
        ind = s_index[0]
        dates, levels = fetch_measure_levels(stations[ind].measure_id, dt=datetime.timedelta(days=dt))
        levels_array = True
        for i in range(len(levels)):
            if type(levels[i]) != float:
                levels_array = False
        if len(dates) == 0 or len(levels) == 0:
            print(f'Dates and/or levels for {stations[ind].name} returned empty from fetch_measure_levels')
        elif levels_array == False:
            print(f'Levels for {stations[ind].name} not returning correct array')
        else:
            plot_water_levels(stations[ind].name, dates, levels)


run()
