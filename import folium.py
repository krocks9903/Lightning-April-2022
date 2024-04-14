import folium
# Create a map centered at a specific location
m = folium.Map(location=[28.4017, -84.0060], zoom_start=10)

# Add a marker at a specific location with a popup
folium.Marker(location=[28.4017, -84.0060], popup="Tampa").add_to(m)

# Display the map
m.save("map4.html")
