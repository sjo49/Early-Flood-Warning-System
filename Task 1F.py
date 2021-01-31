from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistant_typical_range_stations


def run():
    """Requirements for Task 1F"""

    # build station list
    stations = build_station_list()

    # Method within MoniteringStation to check for consistancy
    # for station that is consistant
    print(stations[0].typical_range_consistant())

    # for station that is inconsistant
    print(stations[735].typical_range_consistant())

    # Lisy of stations with inconsistant typical range
    print(inconsistant_typical_range_stations(stations))


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
