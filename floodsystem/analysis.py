from sqlite3 import DateFromTicks
import matplotlib
import numpy
def polyfit(dates,levels,p):
    dateFloat = []
    for date in dates:
        dateFloat.append(matplotlib.dates.date2num(date))
    polyCoeff = numpy.polyfit(date,levels,p)
