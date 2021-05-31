'''
helper function to plot folium map
'''
import folium
import numpy as np
import pandas as pd


# convert dms(degree, minutes, seconds) to dec(decimal) for folium
def dms2dec(latlong_raw):
    var_degree = int(latlong_raw/1e7)
    var_minutes = int(latlong_raw/1e5 - var_degree*100)
    var_seconds = (latlong_raw/1e3 - var_degree*1e4 - var_minutes*100)
    decimal_latlong = var_degree + var_minutes/60 + var_seconds/3600

    return decimal_latlong


# search closest point from points
def closest_node(node, nodes):
    nodes = np.asarray(nodes)
    dist_2 = np.sum((nodes - node)**2, axis=1)
    return np.argmin(dist_2)

# add latitude, longitude to folium map
def addLatLong2map(df_in, color_in, folium_map, legend_name, radius_size):
    lgd_txt = '<span style="color: {col};">{txt}</span>'
    if (len(df_in) > 20000):
        FeatureGroup_in = folium.FeatureGroup(name=lgd_txt.format(txt=legend_name, col=color_in), show=False)
    else:
        FeatureGroup_in = folium.FeatureGroup(name=lgd_txt.format(txt=legend_name, col=color_in))

    nodes = []
    for index_df in range(len(df_in)):
        _latitude = dms2dec(df_in["地点　緯度（北緯）"][index_df])
        _longitude = dms2dec(df_in["地点　経度（東経）"][index_df])
        nodes.append((_latitude, _longitude))
        if (df_in['当事者種別（当事者A）'][index_df] == 61):
            _pedestrian_age = df_in['年齢（当事者A）'][index_df]
        elif (df_in['当事者種別（当事者B）'][index_df] == 61):
            _pedestrian_age = df_in['年齢（当事者B）'][index_df]
        else:
            _pedestrian_age = 999
        gmap_html = 'https://www.google.com/maps/@{0},{1},0a,75y,90t/data=!3m3!1e1!3m1!2e0'.format(_latitude,
                                                                                                   _longitude)
        gmap_str = "<a href='{}'>Link to StreetView</a>".format(gmap_html)

        popup_str = 'location: {0},{1}<br>'.format(_latitude, _longitude) + 'age: {}<br>'.format(_pedestrian_age)
        popup_str += gmap_str

        popup = folium.Popup(popup_str, max_width=1000, show=False)

        folium.CircleMarker([_latitude, _longitude],
                            radius=radius_size, color=color_in, popup=popup,
                            fill=True, fill_opacity=0.9).add_to(FeatureGroup_in)
    folium_map.add_child(FeatureGroup_in)

    '''
    for node_index, node_val in enumerate(nodes):
        nodes.pop(node_index)
        closest_idx = closest_node(node_val, nodes)
        nodes.insert(node_index,node_val)
        #print('node {0} index {1}: value {2}'.format(node_val, closest_idx, nodes[closest_idx]))
    '''

def df_split(df):
    df_person = df[df["事故類型"] == 1].reset_index()
    df_nodeath = df_person[df_person['死者数'] == 0].reset_index()
    del df_nodeath['index']
    df_young_A = df_nodeath[(df_nodeath['当事者種別（当事者A）'] == 61) & (df_nodeath['年齢（当事者A）'] < 56)]
    df_young_B = df_nodeath[(df_nodeath['当事者種別（当事者B）'] == 61) & (df_nodeath['年齢（当事者B）'] < 56)]
    df_young = pd.concat([df_young_A, df_young_B], axis=0).reset_index()
    df_old_A = df_nodeath[(df_nodeath['当事者種別（当事者A）'] == 61) & (df_nodeath['年齢（当事者A）'] > 56)]
    df_old_B = df_nodeath[(df_nodeath['当事者種別（当事者B）'] == 61) & (df_nodeath['年齢（当事者B）'] > 56)]
    df_old = pd.concat([df_old_A, df_old_B], axis=0).reset_index()
    df_death = df_person[df_person['死者数'] > 0].reset_index()

    return df_old, df_young, df_death

# end of code
