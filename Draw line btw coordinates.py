import pygmaps
mymap5 = pygmaps.maps(17.3164945, 57.03219179999999, 15)
latitude_list =[17.343769, 17.307977]
longitude_list =[56.999559, 57.048457]
for i in range(len(latitude_list)) :
  mymap5.addpoint(latitude_list[i], longitude_list[i], "# FF0000")
# list of coordinates         
path = [(17.343769, 57.999559), (17.307977, 57.048457)]
# draw a line in b / w the given coordinates
# 1st argument is list of coordinates
# 2nd argument is colour of the line
mymap5.addpath(path, "# 00FF00")
