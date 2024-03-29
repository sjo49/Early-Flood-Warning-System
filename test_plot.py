from datetime import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit


class Station:
    def __init__(self, name, typical_range):
        self.name = name
        self.typical_range = typical_range


def test_plot_water_levels():
    # test function will deal with inappropriate arguments
    # assume matplotlib will produce figure correctly
    station = 'TestStation'
    dates = [1, 2, 3, 4]  # length of 4
    levels = [0.349, 0.526, 0.573, 0.468, 0.384]  # length of 5
    plot_water_levels(station, dates, levels)  # does not return error then test passes


def test_plot_water_level_with_fit():
    station = Station('TestStation', [0.3, 0.6])
    dates = [datetime(2020, 12, 30), datetime(2020, 12, 31), datetime(2021, 1, 1),
             datetime(2021, 1, 2)]  # length of 4
    levels = [0.349, 0.526, 0.573, 0.468, 0.384]  # length of 5
    p = 4
    plot_water_level_with_fit(station, dates, levels, p)
