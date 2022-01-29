from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
import datetime
from tqdm import tqdm

stations = build_station_list()




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
        else:
            station.latest_level = station.average_value
        levels = []
        while len(levels) < len(dates):
            levels.append(station.latest_level) 
    station.level_history = (dates,levels)

    if len(topTenStations) == 0:
        topTenStations.append(station)
    else:
        for i in range(len(topTenStations)):
            if (station.latest_level - station.average_value) > (topTenStations[i].latest_level - topTenStations[i].average_value):
                topTenStations.insert(i,station)
                count = 1
                break
        if len(topTenStations) <= 10 and count == 0:
            topTenStations.append(station)
        elif len(topTenStations)> 10:
            topTenStations.pop(len(topTenStations)-1)

for station in topTenStations:
    plot_water_levels(station,station.level_history[0],station.level_history[1])
"""   
station = stations[0]
dt = 2
dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
plot_water_levels(station,dates,levels)"""