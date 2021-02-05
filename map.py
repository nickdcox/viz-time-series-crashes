import pandas as pd
import folium
import streamlit as st
from streamlit_folium import folium_static 
from folium import plugins

df_fatal = pd.read_csv('fatal.csv', low_memory=False)

# Create the map.
m = folium.Map(location=[41.8781, -87.6798], zoom_start=12)

# Instantiate a mark cluster object for the crash fatalities.
fatalities = plugins.MarkerCluster().add_to(m)

# Display only crashes where fatalities were reported.
for lat, lng in zip(df_fatal['LATITUDE'], df_fatal['LONGITUDE']):
    folium.Marker(
        location=[lat, lng],
           icon=None,
    ).add_to(fatalities)
    
st.title('Map of Vehicle Crashes with Fatalities in Chicago (2018-2020)')

# Display the map.
folium_static(m)