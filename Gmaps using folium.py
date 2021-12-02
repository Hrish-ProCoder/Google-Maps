import folium

# Map method of folium return Map object

my_map1 = folium.Map(location = [18.6111226, 57.2199794], zoom_start = 14 )

# save method of Map object will create a map
my_map1.save(" my_map6.html " )
