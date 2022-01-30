import floodsystem.stationdata
import floodsystem.datafetcher
import floodsystem.analysis
import floodsystem.plot
import datetime
from tqdm import tqdm

stations = floodsystem.stationdata.build_station_list()
topFive = []
for station in tqdm(stations,desc = 'Loading: '):
    dt = 2
    dates, levels = floodsystem.datafetcher.fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

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

    if len(topFive) == 0:
        topFive.append(station)
    else:
        for i in range(len(topFive)):
            if (station.latest_level - station.average_value) > (topFive[i].latest_level - topFive[i].average_value):
                topFive.insert(i,station)
                count = 1
                break
        if len(topFive) <= 5 and count == 0:
            topFive.append(station)
        elif len(topFive)> 5:
            topFive.pop(len(topFive)-1)
for station in topFive:
    poly, d0 = floodsystem.analysis.polyfit(station.level_history[0],station.level_history[1],4)
    floodsystem.plot.plot_water_levels(station,station.level_history[0],station.level_history[1],poly)
