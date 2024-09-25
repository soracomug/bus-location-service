import lambdasrc.lambda_function
import json
import os

target_area_geojson = """
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          [
            [
              132.71764811654617,
              34.392393437474325
            ],
            [
              132.71764811654617,
              34.40600913685532
            ],
            [
              132.70797187336683,
              34.40600913685532
            ],
            [
              132.70797187336683,
              34.392393437474325
            ],
            [
              132.71764811654617,
              34.392393437474325
            ]
          ]
        ],
        "type": "Polygon"
      }
    }
  ]
}
"""

target_area = json.loads(target_area_geojson)
point_within = lambdasrc.lambda_function.LPoint(132.71309945650137,34.40094244423058)
point_not_within = lambdasrc.lambda_function.LPoint(132.70396764071012,34.39631324093085)

def test_within_area_areaがNoneならFalseを返す():
    assert lambdasrc.lambda_function.within_area(None,point_within) == False

def test_within_area_pointがNoneならFalseを返す():
    assert lambdasrc.lambda_function.within_area(target_area,None) == False

def test_within_area_pointがarea内ならTrueを返す():
    assert lambdasrc.lambda_function.within_area(target_area,point_within) == True

def test_within_area_pointがarea内に無いならFalseを返す():
    assert lambdasrc.lambda_function.within_area(target_area,point_not_within) == False

def test_event_map_to_point_latがないならNoneを返す():
    assert lambdasrc.lambda_function.event_map_to_point({'lon':132.71309945650137}) == None
    assert lambdasrc.lambda_function.event_map_to_point({'lon':132.71309945650137,'lat':None}) == None

def test_event_map_to_point_lonがないならNoneを返す():
    assert lambdasrc.lambda_function.event_map_to_point({'lat':34.40094244423058}) == None
    assert lambdasrc.lambda_function.event_map_to_point({'lat':34.40094244423058,'lon':None}) == None

def test_event_map_to_point_lat_lonがあるならLPointを返す():
    p=lambdasrc.lambda_function.event_map_to_point({'lat':point_within.lat,'lon':point_within.lon})
    assert p.lat == point_within.lat and p.lon == point_within.lon

def test_lambda_handler():
    event = {'lat':point_within.lat,'lon':point_within.lon}
    os.environ['area'] = target_area_geojson
    assert lambdasrc.lambda_function.lambda_handler(event,None) == {'within_area': True}
