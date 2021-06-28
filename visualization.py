import pandas as pd
from HosInfo import HospitalInfor
import folium
from folium.plugins import TimestampedGeoJson
import numpy as np

HospitalInfor = pd.DataFrame(HospitalInfor)


def dataViz(covid, geodata):
    df_con = pd.DataFrame(covid)
    df_on = pd.DataFrame(covid)

    df_con = prepare_df_date(df_con)
    df_on = prepare_df_date(df_on)

    features1 = create_geojson_feature(df_con, df_on)
    make_map(features1, geodata, caption="Corona Kr,2020")


def prepare_df_date(df):
    df['date'] = pd.to_datetime(df['date'])
    df['Confirmed'] = df['Confirmed'].fillna(0)
    return df


def create_geojson_feature(df_con, df_on, radius_max=1000, radius_min=2, fill_color_confirmed='#FC766AFF', weight=1,
                           fill_opacity=0.5):
    features = []

    # for _, row in df_con.iterrows():
    #  radius = np.sqrt(row['Confirmed'])
    # confirmed = row['Confirmed']
    # if 0 < confirmed < 10:
    #     fill_color_confirmed = '#affa79'
    # elif 10 < confirmed < 20:
    #     fill_color_confirmed = '#eded3f'
    # if radius != 0:
    #     radius = radius*50
    # popup = str(row['HosName']) + str(row['Confirmed'])
    # size = [20, radius]
    # feature = {
    #     'type': 'Feature',
    #     'geometry': {
    #         'type': 'Point',
    #         'coordinates': [row['lng'], row['lat']]
    #     },
    #     'properties': {
    #         'time': row['date'].__str__(),
    #         'style': {'color': fill_color_confirmed},
    #         'icon': 'marker',
    #         'iconstyle': {
    #             'iconUrl': 'C:/Users/zxc78/Desktop/vscode/graph.png',
    #             #'fillColor': fill_color_confirmed,
    #             'fillOpacity': 0.1,
    #             #'stroke': 'true',`
    #             #'weight': weight,
    #             'iconSize': size,
    #             #'radius': radius,
    #             'Popup': popup
    #         }
    #     }
    # }
    # features.append(feature)
    a = './pngList/red.png'
    for _, row in df_on.iterrows():
        radius = np.sqrt(row['Confirmed'])
        confirmed = row['Confirmed']
        if 0 < confirmed < 10:
            a = './pngList/yellow.png'
        elif 10 < confirmed < 20:
            a = './pngList/red.png'
        if radius != 0:
            radius = radius * 50
        popups = str(row['HosName']) + str(row['Confirmed'])
        size = [30, radius]
        coordinates = [row['lng'], row['lat']]
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['lng'], row['lat']]
            },
            'properties': {
                'time': row['date'].__str__(),
                'style': {'color': fill_color_confirmed},
                #'icon': 'marker',
                'icon': 'rectangle',
                'iconstyle': {
                    # 'https://cdn.iconscout.com/icon/premium/png-512-thumb/coronavirus-4-613136.png',
                    #'iconUrl': a,
                    'stroke': 'true',
                    'fillOpacity': 0.1,
                    'bounds': [coordinates,[coordinates[0]+1,coordinates[1]],[coordinates[0]+1,coordinates[1]+1],[coordinates[0],coordinates[1]+1]],
                    #'iconSize': size,
                    'weight': weight,
                    'Popup': popups
                }
            }
        }
        features.append(feature)

    return features


def make_map(features, geodata, caption):
    coords = [37.48978019964049, 126.7615853114597]
    map = folium.Map(location=coords, control_scale=True, zoom_start=14, tiles='cartodbpositron', detect_ratina=True)

    folium.Choropleth(
        geo_data=geodata,
        name='choropleth',
        key_on='feature.propeties.name',
        fill_color='yellow',
        fill_opacity=0.15,
        line_opacity=0.7,
        legend_name='처리 수'
    ).add_to(map)

    folium.Circle(
        location=coords,
        color="#000",
        radius=3000
    ).add_to(map)

    TimestampedGeoJson(
        {
            'type': 'FeatureCollection',
            'features': features
        },
        period='PT1M',
        duration='PT1M',
        add_last_point=True,
        auto_play=False,
        loop=False,
        max_speed=1,
        loop_button=True,
        time_slider_drag_update=True,
        transition_time=500  # 반복시간
    ).add_to(map)

    map.caption = caption
    map.save('Corona_kr.html')
