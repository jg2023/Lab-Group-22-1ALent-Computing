from floodsystem import geo
from floodsystem import stationdata
def run():
    stations = stationdata.build_station_list()
    stations_by_river = geo.stations_by_river(stations) # create a dictionary with the key as the river name and the value as a list of stations on that river
    print('\n\n')
    print('River Aire:',stations_by_river['River Aire'],'\n')
    print('River Cam:',stations_by_river['River Cam'],'\n')
    print('River Thames: ',stations_by_river['River Thames'],'\n')

if __name__ == '__main__':
    run()