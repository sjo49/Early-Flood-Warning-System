# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
import math
def stations_by_distance(stations, p):
    tuple_list = []
    for station in range(len(stations):
        def distance(station):
            R = 6373.0
            lat1 = station.coord[0]
            lon1 = station.coord[1]
            lat2 = p[0]
            lon2 = p[1]
            dlat = lat2 - lat1
            dlon = lon2 - lon1
            a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = R * c
            return distance
        tuple_list += (station.name, distance(station))
        return tuple_list.utils.sorted_by_key[1]

