from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

stations = build_station_list()
rivers = rivers_with_station(stations)
print(rivers)
print(len(rivers))

stations_on_each_river = stations_by_river(stations)
print(stations_on_each_river['River Thames'])
