# extracts city name and state name as a string concatination
def extractCityStateNames(line):
    pieces = line.split(",")
    return pieces[0] + pieces[1][:3]
# extracts lattitude and longitude as two integers
def extractCoordinates(line):
    pieces = line.split(",")
    return [int(pieces[1].split("[")[1]), int(pieces[2].split("]")[0])]
# extracts city location as an integer
def extractPopulation(line):
    pieces = line.split(",")
    return int(pieces[2].split("]")[1])
# loads data from miles.dat and uses previous functions to store data
# into 4 passed in data structures
def loadData(cityList, coordList, popList, distanceList):
    f = open("miles.dat")
    
    # Tracks which city we are currently processing
    cityIndex = 0
    
    # Keeps track of distances from current city to previous cities
    distances = []
    distanceList.append([])
    
    # Reads from the file, one line at a time
    for line in f:
        
        # Checks if the line is a "city line", contains information about
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
        
        # Checks if the line is a "distance line", contains information
        # distances from this city to previous cities            
        elif line[0].isdigit():
            distances.extend([int(x) for x in line.split()])
            
    # Distances from the previous city need to be loaded into distanceList
    if distances != []:
        distanceList.append(distances[::-1])
            
# returns integer coords of the passed in city
def getCoordinates(cityList, coordList, name):
    return coordList[cityList.index(name)]
# returns integer coords of the passed in city
def getPopulation(cityList, popList, name):
    return popList[cityList.index(name)]
# returns distance between two cities as an integer    
def getDistance(cityList, distanceList, name1, name2):
    index1 = cityList.index(name1)
    index2 = cityList.index(name2)
    
    if index1 == index2:
        return 0
    elif index1 < index2:
        return distanceList[index2][index1]
    else:
        return distanceList[index1][index2]
# returns the list of cities nearby within the radius 'r' that is passed in 
# as a parameter.
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
