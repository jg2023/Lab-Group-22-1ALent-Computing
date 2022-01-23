# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    rivers = sorted(rivers)
    return rivers

def stations_by_river(stations):
    rivers = rivers_with_station(stations)
    river_dictionary = {}
    for river in rivers:
        river_dictionary[river] = []
    for station in stations:
        river_dictionary[station.river].append(station.name)
    return river_dictionary

def rivers_by_station_number(stations,N):
    riverList = stations_by_river(stations)
    riverStationCount = []
    for river in riverList:
        riverStationCount.append((river,len(riverList[river])))
    riverStationCount.sort(key = lambda x:x[1])
    riverStationCount.reverse()
    if N>0:
        outputList = riverStationCount[0:N]
        count = 0
        if len(outputList) < len(riverStationCount):
            while outputList[len(outputList)-1][1] == riverStationCount[N][1]+count:
                outputList.append(riverStationCount[N+count])
                count +=1
        return outputList
    return None