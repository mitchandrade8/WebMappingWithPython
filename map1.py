import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# Function for elevation map color
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[40.40, -104.73], zoom_start = 6, titles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt, ln], popup = str(el)+"m", fill_color = color_producer(el), color = 'grey', fill_opacity = 0.7))

#for coordinates in [[40.40, -104.73], [39.7392, -104.99],[40.585258, -105.084419], [40.397789, -105.075066], [40.014984, -105.270546]]:
   # fg.add_child(folium.Marker(location = coordinates, popup = "Location", icon = folium.Icon(color = 'black')))
#fg.add_child(folium.Marker(location=[40.40, -104.73], popup = "Greeley", icon = folium.Icon(color = 'beige')))
#fg.add_child(folium.Marker(location=[39.7392, -104.99], popup = "Denver", icon = folium.Icon(color = 'black')))

fgp = folium.FeatureGroup(name= "Population")

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
                           style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")