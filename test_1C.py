from Task1C import run
from floodsystem.stationdata import build_station_list


def test_run():
    assert run()[5] == 'Dernford'


test_run()
