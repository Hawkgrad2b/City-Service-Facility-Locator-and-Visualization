#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:13:40 2023

@author: Sriram Pemmaraju
"""

#-------------------------------------------------------
from project1Phase1 import *
#-------------------------------------------------------

# main program
cityList = []
coordList = []
popList = []
distanceList = []

loadData(cityList, coordList, popList, distanceList)


tests = []
# Test 1
tests.append(getCoordinates(cityList, coordList, "Youngstown OH") == [4110, 8065])

# Test 2
tests.append(getPopulation(cityList, popList, "Youngstown OH") == 115436)

# Test 3
tests.append(getDistance(cityList, distanceList, "Youngstown OH", "Ravenna OH") == 34)

# Test 4
tests.append(getDistance(cityList, distanceList, "Youngstown OH", "Youngstown OH") == 0)

# Test 5
tests.append(getDistance(cityList, distanceList, "Youngstown OH", "Yankton SD") == 966)

# Test 6
tests.append(getCoordinates(cityList, coordList, "Wisconsin Dells WI") == [4363, 8977])

# Test 7
tests.append(getPopulation(cityList, popList, "Wisconsin Dells WI") == 2521)

# Test 8
tests.append(getCoordinates(cityList, coordList, "Ravenna OH") == [4116, 8124])

# Test 9
tests.append(getPopulation(cityList, popList, "Ravenna OH") == 11987)

# Test 10
tests.append(nearbyCities(cityList, distanceList, "Youngstown OH", 100.0) == ['Wheeling WV', 'Steubenville OH', 'Ravenna OH'])

# Test 11
tests.append(getDistance(cityList, distanceList, "Youngstown OH",'Steubenville OH') == 60)

# Test 12
tests.append(getDistance(cityList, distanceList, "Youngstown OH",'Wheeling WV') == 85)

# Test 13
tests.append(nearbyCities(cityList, distanceList, "Waterloo IA", 200.0) == ['Saint Paul MN', 'Rockford IL', 'Rochester MN'])

# Test 14
tests.append(nearbyCities(cityList, distanceList, "San Francisco CA", 100.0) == ['Stockton CA', 'Santa Rosa CA', 'San Jose CA', 'Sacramento CA'])

# Test 15
tests.append(nearbyCities(cityList, distanceList, "Waco TX", 200) == ['Tyler TX', 'Sherman TX', 'San Antonio TX'])

# Test 16
tests.append(len(nearbyCities(cityList, distanceList, "Waco TX",20000)) == 127)

# Test 17
tests.append(len(nearbyCities(cityList, distanceList, "Winston-Salem NC", 0)) == 0)

# Test 18
tests.append(("Waterloo IA" in nearbyCities(cityList, distanceList, "Waterbury CT", 1190)) == True)

# Test 19
tests.append(("Walla Walla WA" in nearbyCities(cityList, distanceList,"Waterbury CT", 1190)) == False)

# Test 20
tests.append(getDistance(cityList, distanceList, "Valdosta GA", "Valley City ND") == 1648)

# Test 21
tests.append(getDistance(cityList, distanceList, "Tampa FL", "Tallahassee FL") == 245)

# Test 22
tests.append((getCoordinates(cityList, coordList, "Utica NY")[0] > getCoordinates(cityList, coordList, "Waco TX")[0]) == True)

# Test 23
tests.append(nearbyCities(cityList, distanceList, "Saint Johnsbury VT", 150) == ['Rutland VT'])

# Test 24
tests.append([getPopulation(cityList, popList, x) for x in nearbyCities(cityList, distanceList, "Utica NY", 100)] == [27861, 170105, 67972])

# Test 25
tests.append(sum([getPopulation(cityList, popList, x) for x in nearbyCities(cityList, distanceList, "Salisbury MD", 20000)]) + getPopulation(cityList, popList, "Salisbury MD") == 15344591)

# Test 26
tests.append(sum([getPopulation(cityList, popList, x) for x in nearbyCities(cityList, distanceList, "Waco TX", 20000)]) + getPopulation(cityList, popList, "Waco TX") == 15344591)

# Test 27
tests.append([x for x in nearbyCities(cityList, distanceList, "Salina KS", 20000) if "BC" in x] == ['Vancouver BC'])

# Test 28
tests.append([x for x in nearbyCities(cityList, distanceList, "Salina KS", 20000) if x.startswith("San")] == ['Santa Rosa CA', 'Santa Fe NM', 'Santa Barbara CA',  'Santa Ana CA', 'San Jose CA', 'San Francisco CA', 'Sandusky OH', 'San Diego CA',
 'San Bernardino CA', 'San Antonio TX', 'San Angelo TX'])

# Test 29
tests.append([x for x in nearbyCities(cityList, distanceList, "Salina KS", 20000) if "IA" in x] == ['Waterloo IA', 'Sioux City IA'])

# Test 30
tests.append(cityList[[x[0] for x in coordList].index(max([x[0] for x in coordList]))] == 'Regina SK')


# Test 31
tests.append(cityList[[x[0] for x in coordList].index(min([x[0] for x in coordList]))] == 'West Palm Beach FL')

# Output the test results
i = 0
for result in tests:
    if not result:
        print("Test", i + 1, "failed")
    i = i + 1
    
