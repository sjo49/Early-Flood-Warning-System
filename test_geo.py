from floodsystem.geo import distance
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key


stations = build_station_list()


def test_distance():
    assert round(distance((52.2, 0.122), (50.2, -1.74))) == 257


test_distance()


def test_stations_by_distance():
    station_list = stations_by_distance(stations, (51, 0.13))
    assert station_list[0][1] <= station_list[1][1]


test_stations_by_distance()


def test_stations_within_radius():
    near_radius = sorted(stations_within_radius(build_station_list, (51, 0.13), 10))
    assert near_radius[0] == stations_by_distance(build_station_list(), (51, 0.13))[0][0]


test_stations_within_radius()


def test_rivers_with_station():
    rivers = rivers_with_station(stations)
    # alphabetical list of rivers
    assert rivers == sorted(rivers)

    # should have 916 rivers in list
    assert len(rivers) != 0


def test_stations_by_river():
    assert len(stations_by_river(stations)) != 0
    assert len(stations_by_river(stations)['River Thames']) != 0


def test_rivers_by_station_number():
    number_of_stations = rivers_by_station_number(stations, 9)
    assert number_of_stations == sorted_by_key(number_of_stations, 1, True)
    assert rivers_by_station_number(stations, 3)[0][1] > rivers_by_station_number(stations, 3)[1][1]
