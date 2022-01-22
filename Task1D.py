from floodsystem import geo
from floodsystem import stationdata
stations = stationdata.build_station_list()
print(len(geo.rivers_with_station(stations)))
print(geo.rivers_with_station(stations))
stations_by_river = geo.stations_by_river(stations)
print('River Aire:',stations_by_river['River Aire'])
print('River Cam:',stations_by_river['River Cam'])
print('River Cam: ',stations_by_river['River Thames'])