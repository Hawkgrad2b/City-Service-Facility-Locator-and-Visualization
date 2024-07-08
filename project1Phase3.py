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


def placeBallons(facilities, cityList, coordList, f):

    kml = simplekml.Kml()
    style = simplekml.Style()
    style.labelstyle.color = simplekml.Color.purple  # Make the text red
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
    kml.save("visualization3002.kml")

def drawLines(cityList, distanceList, facilities, coordList, f):
    
    #f.write('<style id="blackLine">')
    #f.write('<LineStyle>'>
    #f.write('<color>ff0000ff</color>'>
    #f.write('<width>25</width>')
    #f.write('</LineStyle>')
    #f.write('</style>')
    
    for city in cityList: 
        
        minDistance = 5000
        
        for facility in facilities:
            
            name1 = cityList[cityList.index(city)]
            name2 = facility
            
            distance = getDistance(cityList, distanceList, name1, name2)
                
            if distance < minDistance:
                minDistance = distance
                bestFacility = facility 
                
                
            facilLong = '-'+str(coordList[cityList.index(bestFacility)][1])[:-2]+'.'+str(coordList[cityList.index(bestFacility)][1])[-2:]
     
            facilLat = str(coordList[cityList.index(bestFacility)][0])[:-2]+'.'+str(coordList[cityList.index(bestFacility)][0])[-2:]
            
            cityLong = '-'+str(coordList[cityList.index(city)][1])[:-2]+'.'+str(coordList[cityList.index(city)][1])[-2:]
            
            cityLat = str(coordList[cityList.index(city)][0])[:-2]+'.'+str(coordList[cityList.index(city)][0])[-2:]
     
        
        # let's hardcode our line connection (don't hardcode for phase 3!)
        f.write('<Placemark>')
        f.write('<name>Edge 1</name>')
        f.write('<styleUrl>#blackLine</styleUrl>')
        f.write('<LineString>')
        f.write('<coordinates>'+cityLong+','+cityLat+',0,'+facilLong+','+facilLat+',0</coordinates>')
        f.write('</LineString>')
        f.write('</Placemark>')
        
    
    
def display(facilities, cityList, distanceList, coordList, filename):
    
    f = open(filename, "w")
    
    f.write('<Document>')
    
    
    placeBallons(facilities, cityList, coordList, f)
    drawLines(cityList, distanceList, facilities, coordList, f)
    
    f.write('</Document>')
    f.close()
    
    
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