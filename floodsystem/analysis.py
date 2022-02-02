from sqlite3 import DateFromTicks
import matplotlib
import numpy
def polyfit(dates,levels,p):
    dateFloat = []
    d0 = 0
    for date in dates:
        dateFloat.append(matplotlib.dates.date2num(date))
    polyCoeff = numpy.polyfit(dateFloat,levels,p)
    poly = numpy.poly1d(polyCoeff)
    return poly,d0