from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.floodwarning import risk_level
stations = build_station_list()
update_water_levels(stations)


def run():
    risk_lists = risk_level(stations, 2)
    if len(risk_lists[0]) == 0:
        print('No severe risk towns.')
    else:
        print(f'Severe risk towns:{risk_lists[0]}')
    if len(risk_lists[1]) == 0:
        print('No high risk towns.')
    else:
        print(f'High risk towns:{risk_lists[1]}')
    if len(risk_lists[2]) == 0:
        print('No moderate risk towns.')
    else:
        print(f'Moderate risk towns:{risk_lists[2]}')
    if len(risk_lists[3]) == 0:
        print('No low risk towns.')
    else:
        print(f'Low risk towns:{risk_lists[3]}')


run()
