from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""

    # build station list
    stations = build_station_list()

    # Lisy of stations with inconsistent typical range
    print(inconsistent_typical_range_stations(stations))


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
