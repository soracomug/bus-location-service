from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Polygon, Feature
import json
import os
from lpoint import LPoint

def within_area(area,lpoint:LPoint) -> bool:
    if lpoint is None:
        return False
    if area is None:
        return False

    polygon = Polygon(area['features'][0]['geometry']['coordinates'])
    point = Feature(geometry=Point((lpoint.lon,lpoint.lat)))
    return boolean_point_in_polygon(point, polygon)

def event_map_to_point(event:dict) -> LPoint:
    if 'lat' not in event:
        return None
    if 'lon' not in event:
        return None

    lat = event['lat']
    lon = event['lon']
 
    if lat is None:
        return None
    if lon is None:
        return None
    if isinstance(lon, float) == False:
        return None
    if isinstance(lat, float) == False:
        return None

    return LPoint(lon,lat)

def load_area_json() -> dict:
    area = os.environ.get('area')
    if area is None:
        return {}
    return json.loads(area)

def lambda_handler(event, context):
    print(json.dumps(event))
    point = event_map_to_point(event)
    area = load_area_json()
    within = within_area(area,point)
    print(f'within_area: {within}')
    return {'within_area': within}
