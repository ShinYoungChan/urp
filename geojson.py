
def geoJson(hosList):
    features = []
    for i in range(1, len(hosList)):
        data = {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [hosList[i].lng, hosList[i].lat]},
                'properties': {'name': hosList[i].name}}

        features.append(data)

    geometry = {
        'type': 'FeatureCollection',
        'features': features
    }

    return geometry
