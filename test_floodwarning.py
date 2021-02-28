from floodsystem.floodwarning import risk_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
stations = build_station_list()
update_water_levels(stations)
risks = risk_level(stations, 1)


def test_floodwarning():
    for town in risks[0]:
        assert town.relative_water_level() > 8
    for town in risks[1]:
        assert town.relative_water_level() > 5
    for town in risks[2]:
        assert town.relative_water_level() > 2
