# import function from module geo
from floodsystem.geo import stations_by_distance

# import sort function from module utils
from floodsystem.utils import sorted_by_key

# import station list from station data
from floodsystem.stationdata import build_station_list
stations = build_station_list()

def run():
    list_stations = stations_by_distance(stations, (52.2053, 0.1218))
    # slice list to get 10 closest and farthest stations
    list_close_far = []
    list_close_far.extend(list_stations[:10])
    list_close_far.extend(list_stations[-10:])
    print(list_close_far)
    list_town = []
    # find town corresponding with station
    for i in range(len(list_close_far)):
        for j in range(len(stations)):
            if list_close_far[i][0] in stations[j].name:
                list_town.append((list_close_far[i][0], stations[j].town, list_close_far[i][1]))
    # return list sorted by distance
    return sorted_by_key(list_town, 2)
print(run())