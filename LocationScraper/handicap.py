import re
import random
f = open('HandicapCoordinates.txt', 'r')
a = open("latcoord.txt", 'w')
b = open("longcoord.txt", 'w')
f_line = f.readlines()

file = open('BUcoord.txt', 'r')
c = open("latBUcoord.txt", 'w')
d = open("longBUcoord.txt", 'w')
file_line = file.readlines()

#latitudes = []
#longitudes = []
for x in f_line:
    long = re.search('long_wgs84: (-\d\d\.\d*)', x)
    b.write(long.group(1)+"\n")

    lat = re.search('lat_wgs84: (\d\d\.\d*)', x)
    a.write(lat.group(1)+"\n")

for y in file_line:
    longBU = re.search('lng: "(-\d\d\.\d*)', y)
    d.write(longBU.group(1) + "\n")

    latBU = re.search('lat: "(\d\d\.\d*)', y)
    c.write(latBU.group(1) + "\n")

#FOR DEBUGGING PURPOSES
    #latitudes.append(lat.group(1))
    #longitudes.append(long.group(1))
#mMap.addMarker(new MarkerOptions().position(new LatLng(42.36,-71))
#i = 0
#for marker in zip(latitudes,longitudes):
 #   print("mMap.addMarker(new MarkerOptions().position(new LatLng("+str(marker[0])+','+ str(marker[1])+')).title("'+str(i)+'").icon(BitmapDescriptorFactory.defaultMarker('+str(random.randint(0,300))+')));')
  #  i +=1

f.close()
a.close()
b.close()
c.close()
d.close()