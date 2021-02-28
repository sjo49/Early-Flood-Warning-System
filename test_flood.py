from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
stations = build_station_list()


def test_stations_level_over_threshold():
    levels = stations_level_over_threshold(stations, 0.5)
    for i in levels:
        assert [i][1] >= 0.5
        assert [i][1] >= [i + 1][1]


test_stations_level_over_threshold()


def test_stations_highest_rel_level():
    levels = stations_highest_rel_level(stations, 20)
    assert len(levels) == 20
    for i in levels:
        assert [i][1] >= [i + 1][1]


test_stations_highest_rel_level()
