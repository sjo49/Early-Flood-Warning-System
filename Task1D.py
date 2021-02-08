from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river


def run():
    """Requirements for Task 1D"""

    # build station list
    stations = build_station_list()

    # build list of rivers with monitering staitons
    rivers = rivers_with_station(stations)
    print(f"{len(rivers)} stations. First 10 - {rivers[:10]}")

    # dictionary of rivers to a list of the stations on that river
    stations_on_each_river = stations_by_river(stations)
    print(stations_on_each_river['River Aire'])
    print(stations_on_each_river['River Cam'])
    print(stations_on_each_river['River Thames'])


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
