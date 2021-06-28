import math


def degree2radius(degree):
    return degree * (math.pi / 180)


def getDistance(lat1, lng1, lat2, lng2):
    earthR = 6371
    dLat = degree2radius(lat2 - lat1)
    dLng = degree2radius(lng2 - lng1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(degree2radius(lat1)) * math.cos(
        degree2radius(lat2)) * math.sin(dLng / 2) * math.sin(dLng / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earthR * c
    return distance
