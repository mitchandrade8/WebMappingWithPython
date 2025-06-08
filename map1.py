import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


map = folium.Map(location=[40.40, -104.73], zoom_start = 6, titles = "Stamen Terrain")

fg = folium.FeatureGroup(name="Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location = [lt, ln], popup = el, icon = folium.Icon(color = 'black')))

#for coordinates in [[40.40, -104.73], [39.7392, -104.99],[40.585258, -105.084419], [40.397789, -105.075066], [40.014984, -105.270546]]:
   # fg.add_child(folium.Marker(location = coordinates, popup = "Location", icon = folium.Icon(color = 'black')))
#fg.add_child(folium.Marker(location=[40.40, -104.73], popup = "Greeley", icon = folium.Icon(color = 'beige')))
#fg.add_child(folium.Marker(location=[39.7392, -104.99], popup = "Denver", icon = folium.Icon(color = 'black')))
map.add_child(fg)

map.save("Map1.html")