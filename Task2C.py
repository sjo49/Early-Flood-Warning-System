from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
stations = build_station_list()
from floodsystem.stationdata import update_water_levels
update_water_levels(stations)


def run():
    risk_list = stations_highest_rel_level(stations, 10)
    for i in risk_list:
        print(i[0], i[1])


if __name__ == '__main__':
    run()