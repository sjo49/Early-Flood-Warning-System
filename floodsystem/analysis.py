import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    # dates between which the levels will be computed to fit to a polynomial
    date_floats = matplotlib.dates.date2num(dates)
    x = date_floats
    y = levels
    p_coeff = np.polyfit(x-x[0], y, p)
    poly = np.poly1d(p_coeff)
    # d0 is shift of date axis - date axis shifted by x[0] to left
    d0 = -x[0]

    return poly, d0
