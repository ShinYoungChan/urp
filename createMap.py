import folium
from pandas import DataFrame
from distance import getDistance
from HosInfo import HospitalInfor
import Hospital
from delaunay import delaunay
import numpy as np
from folium import plugins

HospitalInfor = DataFrame(HospitalInfor)


def map():
    HospitalInfor
    # 시흥초등학교
    m = folium.Map(location=[37.48978019964049, 126.7615853114597], zoom_start=13)
    lat = 37.48978019964049
    lng = 126.7615853114597
    hosList = [Hospital.Hospital(lat, lng, 0, "발생지역")]
    folium.Marker([lat, lng], title="발생지역", tooltip="발생지역").add_to(m)
    folium.Circle(
        location=[lat, lng],
        color="#000",
        radius=3000
    ).add_to(m)
    latlngList = [[lat, lng]]
    for i in HospitalInfor.index:
        sub_lat = HospitalInfor.loc[i, 'lat']
        sub_lng = HospitalInfor.loc[i, 'lng']
        if getDistance(lat, lng, sub_lat, sub_lng) < 3:
            title = HospitalInfor.loc[i, 'HosName']
            folium.Marker([sub_lat, sub_lng], title=title, tooltip=title).add_to(m)
            hosList.append(Hospital.Hospital(sub_lat, sub_lng, HospitalInfor.loc[i, "capacity"], title))
            latlngList.append([sub_lat, sub_lng])

    dt = delaunay(latlngList)
    length = len(dt.simplices)
    for i in range(length):
        lines = []
        for a in range(3):
            num = dt.simplices[i:i + 1, a][np.array(0)]
            lines.append(latlngList[num])
        folium.Polygon(
            locations=lines
        ).add_to(m)

    plugins.LocateControl().add_to(m)
    m.save("exam.html")
    return hosList, dt