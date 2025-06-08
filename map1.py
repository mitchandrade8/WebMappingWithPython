
import folium
map = folium.Map(location=[40.40, -104.73], zoom_start = 6, titles = "Stamen Terrain")

fg = folium.FeatureGroup(name="Map")
fg.add_child(folium.Marker(location=[40.40, -104.73], popup = "Welcome!", icon = folium.Icon(color = 'green')))
map.add_child(fg)

map.save("Map1.html")