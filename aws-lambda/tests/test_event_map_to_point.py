import lambdasrc.lambda_function
import json
import os

point_within = lambdasrc.lambda_function.LPoint(132.71309945650137,34.40094244423058)

def test_event_map_to_point_latがないならNoneを返す():
    assert lambdasrc.lambda_function.event_map_to_point({'lon':132.71309945650137}) == None
    assert lambdasrc.lambda_function.event_map_to_point({'lon':132.71309945650137,'lat':None}) == None

def test_event_map_to_point_lonがないならNoneを返す():
    assert lambdasrc.lambda_function.event_map_to_point({'lat':34.40094244423058}) == None
    assert lambdasrc.lambda_function.event_map_to_point({'lat':34.40094244423058,'lon':None}) == None

def test_event_map_to_point_lat_lonがあるならLPointを返す():
    p=lambdasrc.lambda_function.event_map_to_point({'lat':point_within.lat,'lon':point_within.lon})
    assert p.lat == point_within.lat and p.lon == point_within.lon
