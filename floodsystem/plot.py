import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def plot_water_levels(station, dates, levels):
    t = dates
    level = levels

    # Plot
    plt.plot(t, level)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    return plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    # dates between which the levels will be computed to fit to a polynomial
    date_floats = matplotlib.dates.date2num(dates)
    x = date_floats
    y = levels
    p_coeff = np.polyfit(x-x[0], y, p)
    poly = np.poly1d(p_coeff)

    x1 = np.linspace(x[0], x[-1], 30)
    typical_low, = plt.plot(x1, np.full(30, station.typical_range[0]), 'g')
    typical_high, = plt.plot(x1, np.full(30, station.typical_range[1]), 'r')
    poly_plot, = plt.plot(x1, poly(x1-x[0]), 'bo')
    plt.legend([typical_low, typical_high, poly_plot],
               ['typical low level', 'typical high level', 'best-fit polynomial'])
    plt.xlabel('dates')
    plt.ylabel('polynomial fit')
    plt.xticks(rotation=45)
    plt.title(f'{station.name} - water level best-fit polynomial')
    plt.tight_layout()

    return plt.show()
