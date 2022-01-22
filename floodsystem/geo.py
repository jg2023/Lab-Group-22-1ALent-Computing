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
        for station in stations:
            if station.river in river_dictionary:
                river_dictionary[river] = river_dictionary[river] + [station]
            else:
                river_dictionary[river] = [station]
    return river_dictionary