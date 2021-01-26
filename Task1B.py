# import function from module geo
from floodsystem.geo import stations_by_distance
# import station list from station data
from floodsystem.stationdata import build_station_list
def run(p):
    list = stations_by_distance(build_station_list, p)
    # slice list to get 10 closest and farthest stations
    list_close_far = list[:10] + list[-10:]
    list_town = []
    # loop over to include name of town
    for i in range(len(list_close_far)):
        list_town[i] = (list_close_far[0], list_close_far[0].town, list_close_far[1])
    print(list_town)



if __name__ == '__main__':
    run((50.2, -5.2))
    print(stations_by_distance(build_station_list, (50.2, -5.2)))



