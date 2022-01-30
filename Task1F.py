from floodsystem import geo
from floodsystem import stationdata
from floodsystem import station
stations = stationdata.build_station_list()
List = station.inconsistent_typical_range_stations(stations)
print(List)
ListOfNames = []
for Station in List:
    ListOfNames.append(Station.name)
print(sorted(ListOfNames))