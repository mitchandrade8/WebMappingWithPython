
import folium
map = folium.Map(location=[40.40, -104.73], zoom_start = 6, titles = "Stamen Terrain")

map.add_child(folium.Marker(location=[40.40, -104.73], popup = "Welcome!", icon = folium.Icon(color = 'green')))

map.save("Map1.html")