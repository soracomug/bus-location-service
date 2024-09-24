class Point():
    def __init__(self, lon, lat):
        self.lat = lat
        self.lon = lon

def within_area(area,point:Point) -> bool:
    if point is None:
        return False
    if area is None:
        return False
    
    return True

def event_map_to_point(event:dict) -> Point:
    if 'lat' not in event:
        return None
    if 'lon' not in event:
        return None

    return Point(event['lon'],event['lat'])

def hambda_handler(event, context):
    return {'within_area': True}