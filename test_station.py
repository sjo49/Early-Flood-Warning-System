# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

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


def test_typical_range_consistent():
    # # stations[0] at time of writing code had consistent data
    if stations[0].typical_range is None or stations[0].typical_range[0] > stations[0].typical_range[1]:
        assert stations[0].typical_range_consistent() is False
    else:
        assert stations[0].typical_range_consistent() is True

    # stations[735] at time of writing code had inconsistent data
    if stations[735].typical_range is None or stations[735].typical_range[0] > stations[735].typical_range[1]:
        assert stations[735].typical_range_consistent() is False
    else:
        assert stations[735].typical_range_consistent() is True


def test_inconsistent_typical_range_stations():
    assert len(inconsistent_typical_range_stations(stations)) != 0
    i_incon = [x for x, y in enumerate(stations) if y.name == inconsistent_typical_range_stations(stations)[0]][0]
    assert stations[i_incon].typical_range_consistent() is False
