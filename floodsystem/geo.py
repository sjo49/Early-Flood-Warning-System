# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import dateutil
from .utils import sorted_by_key  # noqa
import math
from .stationdata import build_station_list
#from haversine import haversine, Unit


def distance(object, p):
    return haversine(object, p)


def stations_by_distance(stations, p):
    tuple_list = []
    for station in stations:
        tuple_list.append((station.name, distance(station.coord, p)))
    return sorted_by_key(tuple_list, 1)


def stations_within_radius(stations, centre, r):
    near_stations = []
    list_stations = stations()
    for station in list_stations:
        if distance(station.coord, centre) <= r:
            near_stations.append(station.name)
    return near_stations


def rivers_with_station(stations):
    rivers_list = []
    for station in stations:
        rivers_list.append(station.river) #builds list with all rivers
    a = set(rivers_list) #coverting to set removes duplicates
    sorted_rivers = sorted(a) #coverts set into alphabetical list of rivers
    return sorted_rivers


def stations_by_river(stations):
    rivers = rivers_with_station(stations)
    river_dict = dict()
    for i in range(len(rivers)):
        stations_on_river = []
        for j in range(len(stations)):
            if rivers[i] == stations[j].river:
                stations_on_river.append(stations[j].name)
            river_dict[rivers[i]] = sorted(stations_on_river)
    return river_dict


def rivers_by_station_number(stations, N):
    stations_on_rivers_dict = stations_by_river(stations)
    rivers = rivers_with_station(stations)
    num_stations_on_river = []
    top_N_rivers = []
    for i in range(len(rivers)):
        x = 0
        x = len(stations_on_rivers_dict[rivers[i]])
        num_stations_on_river.append(x)
    tuple_list = list(zip(rivers, num_stations_on_river))
    ordered_low_to_high = sorted_by_key(tuple_list, 1)
    ordered_num = ordered_low_to_high[::-1] #reverses list
    #set up list of top N rivers by number of stations
    for i in range(N):
        top_N_rivers.append(ordered_num[i])
    #account for including the next in line if it has same number of stations (until number is less)
    if ordered_num[i+1][1] == ordered_num[i][1]:
        while ordered_num[i+1][1] == ordered_num[i][1]:
            top_N_rivers.append(ordered_num[i+1]) 
            i += 1
            if i > 100:
                break

    return top_N_rivers
