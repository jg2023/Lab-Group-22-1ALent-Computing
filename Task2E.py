from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
import datetime
from tqdm import tqdm

stations = build_station_list()



"""
topTenStations = []
for station in tqdm(stations, desc = "Loading: "):
    dt = 2
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    count = 0
    try:
        station.latest_level = levels[0]
    except:
        if type(levels) == int:
            station.latest_level = levels
        elif type(levels) == str:
            if levels.isdigit():
                station.latest_level = int(levels)
        else:
            station.latest_level = station.average_value


    if len(topTenStations) == 0:
        topTenStations.append((station,dates,levels))
    else:
        for i in range(len(topTenStations)):
            if station.latest_level - station.average_value > topTenStations[i][0].latest_level - topTenStations[i][0].average_value:
                topTenStations.insert(i,(station,dates,levels))
                count = 1
                break
        if len(topTenStations) <= 10 and count == 0:
            topTenStations.append((station,dates,levels))
        elif len(topTenStations)> 10:
            topTenStations.pop(len(topTenStations)-1)

for station in topTenStations:
    plot.plot_water_levels(station[0],stations[1],station[2])
    """
station = stations[0]
dt = 2
dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
plot_water_levels(station,dates,levels)