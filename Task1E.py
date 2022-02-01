from floodsystem import geo
from floodsystem import stationdata

def run():
    stations = stationdata.build_station_list()
    print(geo.rivers_by_station_number(stations,9))

if __name__ == '__main__':
    run()