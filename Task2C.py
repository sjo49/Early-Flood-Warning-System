from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list


def run():
    station_list = stations_highest_rel_level(build_station_list(), 10)
    for station in station_list:
        print(station.name, station.relative_water_level())


if __name__ == '__main__':
    run()