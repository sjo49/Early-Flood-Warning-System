from floodsystem.geo import distance
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
stations = build_station_list()


def test_distance():
    assert round(distance((52.2, 0.122), (50.2, -1.74))) == 257


test_distance()


def test_stations_by_distance():
    station_list = stations_by_distance(stations, (51, 0.13))
    assert station_list[0][1] <= station_list[1][1]


test_stations_by_distance()


def test_stations_within_radius():
    near_radius = stations_within_radius(build_station_list, (51, 0.13), 200)
    assert near_radius[-1] == 'Berkeley'


test_stations_within_radius()
