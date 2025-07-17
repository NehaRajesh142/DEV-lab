import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import requests
import os
print("Downloading world shapefile...")
world_url = "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip"
fixed_world_url = "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
zip_path = "world_shapefile.zip"
extract_dir = "world_shapefile"
r = requests.get(fixed_world_url)
with open(zip_path, "wb") as f:
    f.write(r.content)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)
shapefile_path = os.path.join(extract_dir, "ne_110m_admin_0_countries.shp")
world_map = gpd.read_file(shapefile_path)
world_data = pd.DataFrame({
    'Country': ['United States of America', 'Canada', 'India', 'Brazil', 'China'],
    'Value': [100, 150, 200, 80, 120]
})
india_states_data = pd.DataFrame({
    'State': ['Maharashtra', 'Karnataka', 'Tamil Nadu', 'Uttar Pradesh', 'Gujarat'],
    'Value': [50, 75, 60, 40, 30]
})
india_districts_data = pd.DataFrame({
    'District': ['Mumbai', 'Bengaluru', 'Chennai', 'Lucknow', 'Ahmedabad'],
    'Value': [20, 30, 25, 15, 10]
})
world_data_geo = world_map.merge(world_data, how='left', left_on='NAME', right_on='Country')
india_map = world_map[world_map['NAME'] == 'India'].copy()
india_states_data_geo = india_map.loc[india_map.index.repeat(len(india_states_data))].copy()
india_states_data_geo.reset_index(drop=True, inplace=True)
india_states_data_geo['State'] = india_states_data['State']
india_states_data_geo['Value'] = india_states_data['Value']
india_districts_data_geo = india_map.loc[india_map.index.repeat(len(india_districts_data))].copy()
india_districts_data_geo.reset_index(drop=True, inplace=True)
india_districts_data_geo['District'] = india_districts_data['District']
india_districts_data_geo['Value'] = india_districts_data['Value']
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
axs[0].set_title(' World Data')
world_data_geo.boundary.plot(ax=axs[0], linewidth=0.5)
world_data_geo.plot(column='Value', ax=axs[0], legend=True, cmap='viridis',
                    legend_kwds={'label': "Values by Country"})
axs[1].set_title('🇮🇳 India States Data (Simulated)')
india_states_data_geo.boundary.plot(ax=axs[1], linewidth=0.5)
india_states_data_geo.plot(column='Value', ax=axs[1], legend=True, cmap='YlGnBu',
                           legend_kwds={'label': "Values by State"})
axs[2].set_title(' India Districts Data (Simulated)')
india_districts_data_geo.boundary.plot(ax=axs[2], linewidth=0.5)
india_districts_data_geo.plot(column='Value', ax=axs[2], legend=True, cmap='OrRd',
                              legend_kwds={'label': "Values by District"})
plt.tight_layout()
plt.show()
