# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
        

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistant(self):
        if self.typical_range is None:
            consistant = False
        elif self.typical_range[0] > self.typical_range[1]:
            consistant = False
        else:
            consistant = True
        return consistant

    def relative_water_level(self):
        from .stationdata import build_station_list
        stations = build_station_list()
        from .stationdata import update_water_levels
        update_water_levels(stations)
        for station in stations:
            return station.latest_level
        if self.typical_range is None:
            return None
        elif self.typical_range_consistant == False:
            return None
        elif self.latest_level is None:
            return None
        else:
            return ((self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0]))


def inconsistant_typical_range_stations(stations):
    inconsistant_stations = []
    for i in range(len(stations)):
        if stations[i].typical_range_consistant() is False:
            inconsistant_stations.append(stations[i].name)
    return sorted(inconsistant_stations)
