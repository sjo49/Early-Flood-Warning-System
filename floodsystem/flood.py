from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    over_level = []
    for i in range(len(stations)):
        if stations[i].relative_water_level() is None:
            pass
        elif stations[i].relative_water_level() > tol:
            over_level.append((stations[i].name, stations[i].relative_water_level()))
    return sorted_by_key(over_level, 1, True)


def stations_highest_rel_level(stations, N):
    highest = []
    for i in range(len(stations)):
        if stations[i].relative_water_level() is None:
            pass
        else:
            highest.append((stations[i].name, stations[i].relative_water_level()))
    highest_sorted = sorted_by_key(highest, 1, True)
    highest_cut = highest_sorted[:N]
    return highest_cut
