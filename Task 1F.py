from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
from floodsystem.station import inconsistant_typical_range_stations

stations = build_station_list()

print(stations[0].typical_range_consistant())
print(stations[0].typical_range)
print(inconsistant_typical_range_stations(stations))
