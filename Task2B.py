from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
stations = build_station_list()
from floodsystem.stationdata import update_water_levels
update_water_levels(stations)

print(stations[735].relative_water_level())

def run():
    over_stations = stations_level_over_threshold(stations, 0.8)
    for i in over_stations:
        print(i[0], i[1])


run()
