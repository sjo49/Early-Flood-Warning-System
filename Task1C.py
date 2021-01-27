from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
stations = build_station_list


def run():
    station_list = stations_within_radius(stations, (52.2053, 0.1218), 10000)
    return sorted(station_list)


print(run())
