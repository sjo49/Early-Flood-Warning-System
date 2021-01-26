# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import dateutil
from .utils import sorted_by_key  # noqa
import math

def distance(object, p):
            R = 6373.0
            lat1 = object[0]
            lon1 = object[1]
            lat2 = p[0]
            lon2 = p[1]
            dlat = lat2 - lat1
            dlon = lon2 - lon1
            a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = R * c
            return distance


def stations_by_distance(stationobjects, p):
    tuple_list = []
    for i in range(len(stationobjects)):
        tuple_list.append((stationobjects[i].name, distance(stationobjects[i].coord, p)))
    
    return sorted_by_key(tuple_list, 1)



