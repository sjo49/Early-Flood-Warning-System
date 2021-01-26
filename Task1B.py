# import function from module geo
from floodsystem.geo import stations_by_distance
# import sort function from module utils
from floodsystem.utils import sorted_by_key
# import station list from station data
from floodsystem.stationdata import build_station_list
stations = build_station_list()
def run():
    list_stations = stations_by_distance(stations, (52.2053, 0.1218))
    # slice list to get 10 closest stations
    list_close = []
    list_far = []
    list_close.extend(list_stations[:10])
    list_far.extend(list_stations[-10:])
    list_town_close = []
    list_town_far = []
    # find town corresponding with station
    for i in range(len(list_close)):
        for j in range(len(stations)):
            if list_close[i][0] in stations[j].name:
                list_town_close.append((list_close[i][0], stations[j].town, list_close[i][1]))
    # return list sorted by distance
    # repeat above steps for furthest station
    for x in range(len(list_far)):
        for j in range(len(stations)):
            if list_far[x][0] in stations[j].name:
                list_town_far.append((list_far[x][0], stations[j].town, list_far[x][1]))
    # return list sorted by distance

    
    return sorted_by_key(list_town_close, 2), sorted_by_key(list_town_far, 2)


print(run())