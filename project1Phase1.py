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
