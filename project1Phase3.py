import simplekml

def extractCityStateNames(line):
    pieces = line.split(",")
    return pieces[0] + pieces[1][:3]


def extractCoordinates(line):
    pieces = line.split(",")
    return [int(pieces[1].split("[")[1]), int(pieces[2].split("]")[0])]



def extractPopulation(line):
    pieces = line.split(",")
    return int(pieces[2].split("]")[1])


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



def nearbyCities(cityList, distanceList, name, r):

    result = []    
    i = cityList.index(name)           

    j = 0
    for d in distanceList[i]:                
        if d <= r :                          
            result = result + [cityList[j]]  
        j = j + 1
               
    j = i + 1
    while (j < len(distanceList)):           
        if distanceList[j][i] <= r:          
            result = result + [cityList[j]]  
            
        j = j + 1     

    return result
    
    

def numNotServed(served, cityList, distanceList, name, r):
    #return the number of unserved cities in range of r of city with "name"

    citiesNear = nearbyCities(cityList, distanceList, name, r)
    
    count = 0 
    if served[cityList.index(name)] != True:
        count += 1
        
    for city in citiesNear:
        
        cityIndex = cityList.index(city)
            
        if served[cityIndex] != True:
            count += 1
    
    
    
    return count 

def nextFacility(served, cityList, distanceList, r):
    #return city that can serve the most cities within range r.
    #if no further cities to serve, returns None
    #might use nearbyCities function    
    
    maxCitiesServed =  0
    facilityCity = None
        
    for city in cityList:
        
        #if served[cityList.index(city)] != True:
            
        count = numNotServed(served, cityList, distanceList, city, r)
            
        
        
        if count > maxCitiesServed:
                
            maxCitiesServed = count 
                
            facilityCity = city
    
    
    return facilityCity
    
    
def locateFacilities(cityList, distanceList, r):
    
    numCities = len(cityList)
    served = [False] * numCities
    
    #initialize the list to hold cities where service facilities will be
    facilities = []
    
    while False in served:
        #mark that city as "served", and the cities that are served by this facility as "served" as well.
        #get the next best service facility with the next facility
        
        facility = nextFacility(served, cityList, distanceList, r)
        
        if facility is None:
            print("error")
            break
        
        served[cityList.index(facility)] = True
        
        citiesNear = nearbyCities(cityList, distanceList, facility, r)
        
        for city in citiesNear:
            served[cityList.index(city)] = True
            
            
        facilities.append(facility)
    
    return facilities


def getDistance(cityList, distanceList, name1, name2):
    index1 = cityList.index(name1)
    index2 = cityList.index(name2)
    
    if index1 == index2:
        return 0
    elif index1 < index2:
        return distanceList[index2][index1]
    else:
        return distanceList[index1][index2]


def placeBallons(facilities, cityList, coordList, kml):

    style = simplekml.Style()
    style.labelstyle.color = simplekml.Color.purple
    style.labelstyle.scale = 1.5
    style.iconstyle.icon.href = 'https://maps.google.com/mapfiles/kml/pal3/icon21.png'
    style.iconstyle.scale = 2

    for i in range(len(cityList)):
        pnt = kml.newpoint(name= cityList[i])

        latitude = coordList[i][0] / 100.0
        longitude = coordList[i][1] / 100.0

        latitude = round(latitude, 2)
        longitude = round(longitude, 2)
        
        pnt.coords = [(-longitude, latitude)]
        pnt.style = style

def drawLines(cityList, distanceList, facilities, coordList, kml):
    
    for city in cityList: 
        
        minDistance = 5000
        
        for facility in facilities:
            
            name1 = cityList[cityList.index(city)]
            name2 = facility
            
            distance = getDistance(cityList, distanceList, name1, name2)
                
            if distance < minDistance:
                minDistance = distance
                bestFacility = facility 
                
                
            facility_index = cityList.index(bestFacility)
            city_index = cityList.index(city) 

            facilityLongitude = -coordList[facility_index][1] / 100.0
            facilityLatitude = coordList[facility_index][0] / 100.0

            cityLongitude = -coordList[city_index][1] / 100.0
            cityLatitude = coordList[city_index][0] / 100.0

        line = kml.newlinestring(name= f"{city} to {facility}")
        line.coords = [(cityLongitude,cityLatitude),(facilityLongitude, facilityLatitude)]
        line.style.linestyle.color = '990000ff'
    
    
def display(facilities, cityList, distanceList, coordList, filename):
    
    kml = simplekml.Kml()    
    
    placeBallons(facilities, cityList, coordList, kml)
    drawLines(cityList, distanceList, facilities, coordList, kml)
    
    kml.save(filename)
    
    
def main():
    
    cityList = []
    coordList = []
    popList = []
    distanceList = []
    
    loadData(cityList, coordList, popList, distanceList)
    
    facilities = locateFacilities(cityList, distanceList, 300)
    display(facilities, cityList, distanceList, coordList, "visualization300.kml")
    
    facilities = locateFacilities(cityList, distanceList, 800)
    display(facilities, cityList, distanceList, coordList, "visualization800.kml")

main()