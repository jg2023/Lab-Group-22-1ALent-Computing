from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import datetime


stations = build_station_list()

for station in stations:
    print(station)

'''
dt = 2
dates, levels = fetch_measure_levels(
station.measure_id, dt=datetime.timedelta(days=dt))'''