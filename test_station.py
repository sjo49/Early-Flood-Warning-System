# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistant_typical_range_stations

stations = build_station_list()


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistant():
    # stations[0] is has consistant typical range data
    assert stations[0].typical_range_consistant() is True

    # stations[735] has inconsistant typical range data
    assert stations[735].typical_range_consistant() is False


def test_inconsistant_typical_range_stations():
    assert len(inconsistant_typical_range_stations(stations)) != 0
    assert stations[735].name in inconsistant_typical_range_stations(stations)
