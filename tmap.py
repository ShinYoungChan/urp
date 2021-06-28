import requests
import json
from json import loads


def timeSet(startLat, startLng, endLat, endLng):
    url = "https://apis.openapi.sk.com/tmap/routes"

    headers = {
        "appkey": "l7xx3f5a054e4ce5415591e8ec0abaf942f5",
        "version": "1",
        "callback": ""
    }

    payload = {
        "roadType": 32,
        "directionOption": 1,
        "endX": endLng,
        "endY": endLat,
        "startX": startLng,
        "startY": startLat
    }

    r = requests.post(url, json=payload, headers=headers)

    jsonObj = json.loads(r.text)

    time = round(int(jsonObj['features'][0]['properties']['totalTime']) / 60)

    return time
