# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    """This function creates a set containing all the river names which have a station on it. 
    It is set up so each river only occurs onece """
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    rivers = sorted(rivers)
    return rivers

def stations_by_river(stations):
    """This function creates a dictionary with river names as a key and a list of all the 
    station names on the respective river"""
    rivers = rivers_with_station(stations)
    river_dictionary = {}
    for river in rivers:
        river_dictionary[river] = [] #Generating Dictionary
    for station in stations:
        river_dictionary[station.river].append(station.name) #Assigning values
    return river_dictionary

def rivers_by_station_number(stations,N):
    """This Function generates a list of tuples (River Name, Number of Stations) 
    ordered from highest number to lowest number of stations. It then takes the first N rivers and outputs their 
    names and numbers. Including extra rivers if they have the same number of stations as the Nth one"""
    riverList = stations_by_river(stations)
    riverStationCount = []
    for river in riverList:
        riverStationCount.append((river,len(riverList[river]))) 
    riverStationCount.sort(key = lambda x:x[1])#Sort into lowest to highest
    riverStationCount.reverse() #Reverse to highest to lowest
    if N>0 and N <= len(riverStationCount): #Error Handling
        outputList = riverStationCount[0:N]
        count = 0
        if len(outputList) < len(riverStationCount): #Error Handling
            while outputList[len(outputList)-1][1] == riverStationCount[N][1]+count:
                outputList.append(riverStationCount[N+count])
                count +=1
        return outputList
    return None