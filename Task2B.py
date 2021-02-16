from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
stations = build_station_list()
from floodsystem.stationdata import update_water_levels
update_water_levels(stations)

print(stations[23].relative_water_level())

def run():
    stations_level_over_threshold(stations, 0.8)


print(run())
