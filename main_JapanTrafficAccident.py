'''
Plot 2019 japan traffic accident into folium map
TODO: analyze death, young accident location
TODO: add dangerous rate, reason, label (no traffic light, narrow pedestrian zone, intersection with blind spot)
TODO: create ranking per selected region for death, young accident, overall accident
'''
import pandas as pd
import folium
import time
# own lib
from helper.constants_JTA import constants_jta
from helper.utils_JTA import df_split, addLatLong2map

# read csv
df = pd.read_csv("./honhyo_2019.csv", encoding='cp932')

# create map
folium_map = folium.Map(location=[constants_jta.Lat_init,
                                  constants_jta.Long_init],
                        zoom_start=constants_jta.Zoom_init,
                        prefer_canvas=True)
# NOTE: rendering speed is greatly improved by prefer_canvas=True in folium.map

# split dataframe
df_old, df_young, df_death = df_split(df)

# add layers to map
start_time = time.time()
# yellow = '#ffa500', red = '#ff0000', black = '#000000'
addLatLong2map(df_old, '#ffa500', folium_map, 'old pedestrian accident', 2)
addLatLong2map(df_young, '#ff0000', folium_map, 'young pedestrian accident', 3)
addLatLong2map(df_death, '#000000', folium_map, 'pedestrian death', 3)
print("--- %s seconds to add layers ---" % (time.time() - start_time))

# turn on layer control
folium_map.add_child(folium.map.LayerControl())

# save map
folium_map.save(constants_jta.Save_path)
print("--- %s seconds until save map ---" % (time.time() - start_time))

# end of code
