from lambdasrc.lambda_function import within_area
from lambdasrc.lpoint import LPoint
import json

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
point_within = LPoint(132.71309945650137,34.40094244423058)
point_not_within = LPoint(132.70396764071012,34.39631324093085)

def test_within_area_areaがNoneならFalseを返す():
    assert within_area(None,point_within) == False

def test_within_area_pointがNoneならFalseを返す():
    assert within_area(target_area,None) == False

def test_within_area_pointがarea内ならTrueを返す():
    assert within_area(target_area,point_within) == True

def test_within_area_pointがarea外ならFalseを返す():
    assert within_area(target_area,point_not_within) == False
