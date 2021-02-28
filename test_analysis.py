from datetime import datetime
from floodsystem.analysis import polyfit


def test_polyfit():
    # assume numpy functons work - test that polyfit function calls correctly
    dates = [datetime(2020, 12, 30), datetime(2020, 12, 31), datetime(2021, 1, 1),
        datetime(2021, 1, 2), datetime(2021, 1, 3)]
    levels = [0.349, 0.526, 0.573, 0.468, 0.384]
    p = 4
    x = polyfit(dates, levels, p)
    print(x)


test_polyfit()
