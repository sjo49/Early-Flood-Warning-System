from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)


def test_stations_level_over_threshold():
    levels = stations_level_over_threshold(stations, 0.5)
    for i in range(len(levels) - 1):
        assert levels[i][1] >= 0.5
        assert levels[i][1] >= levels[i + 1][1]


test_stations_level_over_threshold()


def test_stations_highest_rel_level():
    levels = stations_highest_rel_level(stations, 20)
    assert len(levels) == 20
    for i in range(len(levels) - 1):
        assert levels[i][1] >= levels[i + 1][1]


test_stations_highest_rel_level()
