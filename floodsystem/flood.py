from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    over_level = []
    for station in stations:
        if station.relative_water_level() is None:
            pass
        elif station.relative_water_level() > tol:
            over_level.append((station.name, station.relative_water_level()))
    return sorted_by_key(over_level, 1, True)


def stations_highest_rel_level(stations, N):
    highest = []
    for station in stations:
        highest.append((station.name, station.relative_water_level()))
    highest_sorted = sorted_by_key(highest, 1)
    highest_cut = highest_sorted[:N]
    return highest_cut
