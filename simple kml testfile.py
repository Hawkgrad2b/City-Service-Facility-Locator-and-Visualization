import simplekml


words = ['one', 'two', 'three']
coordinates = [1,1,2,2,3,3,4,4]


#kml = simplekml.Kml()
#pnt = kml.newpoint(name=words[0])
#pnt.coords = [(coordinates[0],coordinates[1])]


kml = simplekml.Kml()
style = simplekml.Style()
style.labelstyle.color = simplekml.Color.red  # Make the text red
style.labelstyle.scale = 1
style.iconstyle.icon.href = 'https://maps.google.com/mapfiles/kml/pal3/icon21.png'
style.iconstyle.scale = 5
i = 0 
for word in words:
    pnt = kml.newpoint(name= word)
    pnt.coords = [(coordinates[i],coordinates[i+1])]
    pnt.style = style
    kml.save("Point Shared Style1.kml")
    i += 2



#kml = simplekml.Kml()
#kml.newpoint(name=words[0], coords=[(coordinates[0],coordinates[1])])  # lon, lat, optional height
#kml.save("botanicalgarden.kml")

""" A geographic location defined by lon, lat, and altitude.

Arguments are the same as the properties.

Usage:

    import simplekml
    kml = simplekml.Kml()
    pnt = kml.newpoint(name='A Point')
    pnt.coords = [(1.0, 2.0)]
    kml.save("Point.kml")
Styling a Single Point:

    import simplekml
    kml = simplekml.Kml()
    pnt = kml.newpoint(name='A Point')
    pnt.coords = [(1.0, 2.0)]
    pnt.style.labelstyle.color = simplekml.Color.red  # Make the text red
    pnt.style.labelstyle.scale = 2  # Make the text twice as big
    pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
    kml.save("Point Styling.kml") 

    Sharing a Style with many Points (Shared Style):

    import simplekml
    kml = simplekml.Kml()
    style = simplekml.Style()
    style.labelstyle.color = simplekml.Color.red  # Make the text red
    style.labelstyle.scale = 2  # Make the text twice as big
    style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
    for lon in range(2):  # Generate longitude values
        for lat in range(2): # Generate latitude values
           pnt = kml.newpoint(name='Point: {0}{0}'.format(lon,lat))
           pnt.coords = [(lon, lat)]
           pnt.style = style
    kml.save("Point Shared Style.kml")
    """