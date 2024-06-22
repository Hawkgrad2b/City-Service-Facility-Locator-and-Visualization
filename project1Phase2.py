#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:15:29 2023

@author: Sriram Pemmaraju
"""

###############################################################################
#
# Specification: This "helper" function extracts the city name and state name
# from the given "city line" and returns these, concatenated in the correct
# format, as a single string.
#
###############################################################################
def extractCityStateNames(line):
    pieces = line.split(",")
    return pieces[0] + pieces[1][:3]

###############################################################################
#
# Specification: This "helper" function extracts the latitude and longitude
# from the given "city line" and returns these, in a size-2 list of integers.
#
###############################################################################
def extractCoordinates(line):
    pieces = line.split(",")
    return [int(pieces[1].split("[")[1]), int(pieces[2].split("]")[0])]


###############################################################################
#
# Specification: This "helper" function extracts the city population
# from the given "city line" and returns this an an integer.
# 
###############################################################################
def extractPopulation(line):
    pieces = line.split(",")
    return int(pieces[2].split("]")[1])

###############################################################################
#
# Specification: Reads information from the files "miles.dat" and loads the data
# structures cityList, coordList, popList, and distanceList with this information.
# Assumes that these 4 data structures are sent in empty.
# 
###############################################################################
def loadData(cityList, coordList, popList, distanceList):
    f = open("miles.dat")
    
    # Tracks which city we are currently processing
    cityIndex = 0
    
    # Keeps track of distances from current city to previous cities
    distances = []
    distanceList.append([])
    
    # Reads from the file, one line at a time
    for line in f:
        
        # Checks if the line is a "city line", i.e., contains information about
        # the city
        if line[0].isalpha():
            
            # Distances from the previous city need to be loaded into distanceList
            if distances != []:
                distanceList.append(distances[::-1])
                distances = []
                
            cityList.append(extractCityStateNames(line))
            coordList.append(extractCoordinates(line))
            popList.append(extractPopulation(line))
            cityIndex = cityIndex + 1
        
        # Checks if the line is a "distance line", i.e., contains information
        # distances from this city to previous cities            
        elif line[0].isdigit():
            distances.extend([int(x) for x in line.split()])
            
    # Distances from the previous city need to be loaded into distanceList
    if distances != []:
        distanceList.append(distances[::-1])
            

###############################################################################
#
# Specification: returns the coordinates (which is a list of 2 integers) of the 
# given city. It assumes that the given city name is in cityList.
#
###############################################################################
def getCoordinates(cityList, coordList, name):
    return coordList[cityList.index(name)]

###############################################################################
#
# Specification: returns the population (which is an integer) of the 
# given city. It assumes that the given city name is in cityList.
#
###############################################################################
def getPopulation(cityList, popList, name):
    return popList[cityList.index(name)]

###############################################################################
#
# Specification: returns the distance (an int) between cities name1 and name2. 
# If name1 and name2 are identical, return 0. It assumes that the given city names
# city1 and city2 are both in cityList.
#
###############################################################################    
def getDistance(cityList, distanceList, name1, name2):
    index1 = cityList.index(name1)
    index2 = cityList.index(name2)
    
    if index1 == index2:
        return 0
    elif index1 < index2:
        return distanceList[index2][index1]
    else:
        return distanceList[index1][index2]

###############################################################################
#
# Specification: The function takes 4 arguments:
#    
# cityList: is a list of strings, representing names of cities.
#
# distanceList: contains distances between pairs of cities in cityist. 
# distanceList has the same length as cityList and each element in distanceList
# is itself a list. Furthermore, distanceList[i] is a list of length i, where
# distanceList[i][j] (0 <= j <= i-1) represents the distance between cityList[i]
# and cityList[j] . 
#
# --------------
# EXAMPLE: cityList = ["X", "A", "B", "Z", "D"]
# distanceList = [[], [95], [170, 125], [150, 80, 225], [110, 175, 210, 120]]
#
# Then distanceList[2] represents the distances between city "B" and cities "X"
# and "A". More specifically, "X" is 170 miles from "B" and "A" is 125 miles from
# "B". 
#
# Note that distances between city "B" and cities "Z" and "D" appear in 
# distanceList[3][2] and distanceList[4][2] respectively. Thus the distance 
# between city "B" and "Z" is 225 and between city "B" and "D" is 210.
# --------------
# 
# name: is a name of a city; you can assume that name will be in cityList
#
# r: is a non-negative floating point number
#
# The function is required to return a list of cities at distance at most r
# from the city name. This list should contain names of cities in the same order
# as they appear in cityList.
#
# --------------
# EXAMPLE: cityList = ["X", "A", "B", "Z", "D"]
# distanceList = [[], [95], [170, 125], [150, 80, 225], [110, 175, 210, 120]]
#
# nearbyCities(cityList, distanceList, "B", 200) returns 
# ['X', 'A']
#
# nearbyCities(cityList, distanceList, "B", 210) returns
# ['X', 'A', 'D']
#
# nearbyCities(cityList, distanceList, "B", 500) returns
# ['X', 'A', 'Z', 'D']
#
# nearbyCities(cityList, distanceList, "X", 150) returns
# ['A', 'Z', 'D']
#
# nearbyCities(cityList, distanceList, "X", 0) returns
# []
#
# nearbyCities(cityList, distanceList, "X", 170) returns
# ['A', 'B', 'Z', 'D']
#
# nearbyCities(cityList, distanceList, "D", 170) returns
# ['X', 'Z']
#
# nearbyCities(cityList, distanceList, "D", 175.5) returns
# ['X', 'A', 'Z']
# 
###############################################################################

def nearbyCities(cityList, distanceList, name, r):

    # The list result will eventually contain the names of cities
    # at distance <= r from name
    result = []
    
    # Get the index of the named city in cityList
    i = cityList.index(name)           
    
    # Walk down the distances between the named city and previous cities
    j = 0
    for d in distanceList[i]:      # For every other previous city
        if d <= r :      # If within r of named city
            result = result + [cityList[j]]  # Add to result
        j = j + 1
        
    # Walk down the distances between the named city and later cities       
    j = i + 1
    while (j < len(distanceList)): # For every other previous city
        if distanceList[j][i] <= r: # If within r of named city
            result = result + [cityList[j]] # Add to result
            
        j = j + 1     

    return result

###############################################################################
#
# Specification: returns the number of unserved cities within distance r of city. 
# This number includes city itself, it has not been served.
# served is a boolean list indicating which cities have been served. CityList is
# the list of city names.
# 
###############################################################################

def numNotserved(served, cityList, distanceList, name, r) :
    
    if served[cityList.index(name)]:
        result = 0
    else:
        result = 1

    # for each city within distance r of city
    for c in nearbyCities(cityList, distanceList, name, r) :
        # if not served, add it to the list of unserved citys
        if not served[cityList.index(c)] :
            result = result + 1
    return result


###############################################################################
#
# Specification: Returns the name of the city that can serve the most as-yet-unserved 
# cities within radius r. Returns None if all cities are served. If there is a tie,
# this function returns the city that appears earliest in cityList 
# 
###############################################################################
def nextFacility(served, cityList, distanceList, r) :

    facility = None      # Name of city that will be the next service facility
    numberServed = 0     # Number of cities that facility will serve

    # For each city
    for c in range(len(cityList)) :
        # compute how many unserved cities will be served by city c
        willBeServed = numNotserved(served, cityList, distanceList, cityList[c], r)
        
        # if it can serve more cities than the previous best city
        if willBeServed >  numberServed:
            # make it the service center
            facility = cityList[c]
            numberServed = willBeServed
    return facility

###############################################################################
#
# Returns an alphabetically sorted list of the cities in which facilities
# must be located to service all cities with a service radius of r. '''
# 
###############################################################################
def locateFacilities(cityList, distanceList, r) :

    # List of cities that are served by current facilities
    served = [False] * len(cityList)

    # List of cities that are service facilities
    facilities = []

    # Get the city that is the next best service facility
    facility = nextFacility(served, cityList, distanceList, r )

    # While there are more cities to be served
    while facility :

        # Mark the service facility as served
        served[cityList.index(facility)] = True

        # Mark each city as served that will be served by this facility
        for city in nearbyCities(cityList, distanceList, facility, r) :
            served[cityList.index(city)] = True

          # Append the city to the list of service facilities
        facilities.append(facility)

        # Get the city that is the next best service facility
        facility = nextFacility(served, cityList, distanceList, r)

    return facilities

# main program
cityList = []
coordList = []
popList = []
distanceList = []

loadData(cityList, coordList, popList, distanceList)



#print(cityList)
#print(coordList)
#print(popList)
#print(distanceList[0], distanceList[1], distanceList[2], distanceList[3])