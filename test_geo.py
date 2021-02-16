from floodsystem.geo import distance
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
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
    near_radius = stations_within_radius(build_station_list, (51, 0.13), 10)
    assert near_radius[0] == 'Goldbridge'


test_stations_within_radius()


def test_rivers_with_station():
    rivers = rivers_with_station(stations)
    # alphabetical list of rivers
    assert rivers == sorted(rivers)

    # should have 916 rivers in list
    assert len(rivers) != 0


def test_stations_by_river():
    # addlestone bourne has two stations: ['Addlestone', 'Grants Bridge']
    assert len(stations_by_river(stations)) != 0
    assert len(stations_by_river(stations)['River Thames']) != 0


def test_rivers_by_station_number():
    # top 3 rivers
    assert rivers_by_station_number(stations, 3) == [('River Thames', 55), ('River Avon', 32), ('River Great Ouse', 30)]

    # should include 11th term when N = 10 because 10th and 11th river both have 17 stations
    assert len(rivers_by_station_number(stations, 10)) == 11
