from lambdasrc.lambda_function import event_map_to_point
from lambdasrc.lpoint import LPoint

point_within = LPoint(132.71309945650137,34.40094244423058)

def test_event_map_to_point_latがないならNoneを返す():
    assert event_map_to_point({'lon':132.71309945650137}) == None
    assert event_map_to_point({'lon':132.71309945650137,'lat':None}) == None

def test_event_map_to_point_lonがないならNoneを返す():
    assert event_map_to_point({'lat':34.40094244423058}) == None
    assert event_map_to_point({'lat':34.40094244423058,'lon':None}) == None

def test_event_map_to_point_latがfloatでないならNoneを返す():
    assert event_map_to_point({'lat':'abcd','lon':132.71309945650137}) == None
    assert event_map_to_point({'lat':34,'lon':132.71309945650137}) == None

def test_event_map_to_point_lonがfloatでないならNoneを返す():
    assert event_map_to_point({'lat':34.40094244423058,'lon':'132.71309945650137'}) == None
    assert event_map_to_point({'lat':34.40094244423058,'lon':132}) == None

def test_event_map_to_point_lat_lonがあるならLPointを返す():
    p = event_map_to_point({'lat':point_within.lat,'lon':point_within.lon})
    assert p.lat == point_within.lat and p.lon == point_within.lon
