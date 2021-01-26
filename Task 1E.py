from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

stations = build_station_list()
rivers = rivers_with_station(stations)
print(rivers_by_station_number(stations, 12))
