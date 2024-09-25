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

point_within = lambdasrc.lambda_function.LPoint(132.71309945650137,34.40094244423058)
point_not_within = lambdasrc.lambda_function.LPoint(132.70396764071012,34.39631324093085)

def test_lambda_handler_pointがarea内ならtrueを返す():
    event = {'lat':point_within.lat,'lon':point_within.lon}
    os.environ['area'] = target_area_geojson
    assert lambdasrc.lambda_function.lambda_handler(event,None) == {'within_area': True}

def test_lambda_handler_pointがarea外ならfalseを返す():
    event = {'lat':point_not_within.lat,'lon':point_not_within.lon}
    os.environ['area'] = target_area_geojson
    assert lambdasrc.lambda_function.lambda_handler(event,None) == {'within_area': False}
