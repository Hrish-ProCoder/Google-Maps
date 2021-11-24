# importing pygmaps
import pygmaps
map2 = pygmaps.maps(17.2156831, 56.03222175623432, 15)

# draw grids on the map

# 1st argument is the starting point of latitude
# 2nd argument is the ending point of latitude
# 3rd argument is grid size in latitude

# 4th argument is the starting point of longitude
# 5th argument is the ending point of longitude
# 6th argument is grid size in longitude

maps2.setgrids(17.23, 17.24, 0.001, 
               56.03, 56.04, 0.001)

map2.draw("pygmap2.html")
