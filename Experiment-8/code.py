import pandas as pd
import plotly.express as px
import json
import requests
world_data = pd.DataFrame({
 'Country': ['India', 'United States', 'Brazil', 'China', 'Australia'],
 'ISO_Code': ['IND', 'USA', 'BRA', 'CHN', 'AUS'],
 'GDP_Trillion': [3.5, 21.4, 2.1, 14.7, 1.4]
})
fig1 = px.choropleth(
 world_data,
 locations='ISO_Code',
 color='GDP_Trillion',
 hover_name='Country',
 color_continuous_scale='Blues',
 title='World Countries by GDP (Trillions USD)',
 projection='natural earth'
)
fig1.show()
india_states_url ='https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson'
india_geojson = requests.get(india_states_url).json()
indian_states_data = pd.DataFrame({
 'State': ['Telangana', 'Andhra Pradesh', 'Karnataka', 'Tamil Nadu'],
 'Population_M': [39.6, 53.6, 67.6, 72.1]
})
fig2 = px.choropleth(
 indian_states_data,
 geojson=india_geojson,
 locations='State',
 featureidkey='properties.NAME_1',
 color='Population_M',
 color_continuous_scale='Viridis',
 title='Indian States by Population (Millions)',
)
fig2.update_geos(fitbounds="locations", visible=False)
fig2.show()
