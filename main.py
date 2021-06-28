from createMap import map
import numpy as np
import algorithm
import HospitalManage
from geojson import geoJson
import numpy as np
from visualization import dataViz


def newVec(index, dt):
    a = [i for i in range(index)]
    # 벡터 생성
    for i in range(index):
        a[i] = []

    length = len(dt.simplices)

    for i in range(length):
        for j in range(3):
            num = dt.simplices[i:i + 1, j][np.array(0)]
            for k in range(3):
                vecNum = dt.simplices[i:i + 1, k][np.array(0)]
                if num == vecNum:
                    continue
                a[num].append(vecNum)

    for i in range(index):
        a[i] = list(set(a[i]))

    return a


patient = int(input("환자 수를 입력하세요."))

# 맵 생성과 병원 수 및 정보 반환
hosList, dt = map()

index = len(hosList)

vec = newVec(index, dt)

algorithm.createMat(index)
end = algorithm.setMat(hosList, vec, index)
algorithm.mcmf(hosList, vec, 0, end, index)

hospitalmanage = HospitalManage.HospitalManage()
hospitalmanage.setHospiatal(hosList)

data = hospitalmanage.process(patient)
covid = {
    'HosName': data.HosName,
    'date': data.date,
    'Confirmed': data.Confirmed,
    'lng': data.lng,
    'lat': data.lat
}

print("최종 처리 수")
for i in range(1, len(hosList)):
    print(hosList[i].name + ": " + str(hosList[i].total))

geoData = geoJson(hosList)

dataViz(covid, geoData)
