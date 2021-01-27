from Task1B import run
from floodsystem.stationdata import build_station_list


def test_run():
    assert run()[0][0] == ('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494)


test_run()
    