from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Polygon, Feature
import json
import os

class LPoint():
    def __init__(self, lon, lat):
        self.lat = lat
        self.lon = lon

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
    if event['lat'] is None:
        return None
    if event['lon'] is None:
        return None

    return LPoint(event['lon'],event['lat'])

def lambda_handler(event, context):
    print(json.dumps(event))
    point = event_map_to_point(event)
    area = json.loads(os.environ['area'])
    return {'within_area': within_area(area,point)}
