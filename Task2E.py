from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import datetime


stations = build_station_list()




topTenStations = []
for station in stations:
    print(station)
    dt = 2
    dates, levels = fetch_measure_levels(
    station.measure_id, dt=datetime.timedelta(days=dt))
    station.latest_level = levels[0]
    try:
        for i in range(len(topTenStations)):
            if station.latest_level - station.average_value > topTenStations[i].latest_level - topTenStations[i].average_value:
                topTenStations.insert(station)
                topTenStations.pop(len(topTenStations))
                break

        
    except:
        topTenStations.append(station)
for station in topTenStations:
    print(station.name,station.level)