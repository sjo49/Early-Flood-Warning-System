from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Requirements for Task 1E"""

    # build station list
    stations = build_station_list()

    # function that resturns top N rivers with the most stations
    print(rivers_by_station_number(stations, 12))


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
