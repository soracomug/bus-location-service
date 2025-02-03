import os
import json
import pytest
from lambdasrc.lambda_function import load_area_json

def test_load_area_json_areaが設定されていない場合は空のJSONを返す(mocker):
    mocker.patch.dict(os.environ, {}, clear=True)
    assert load_area_json() == {}

def test_load_area_json_areaが設定されている場合_json_loadの結果を返す(mocker):
    area_json = '{"type": "FeatureCollection", "features": []}'
    mocker.patch.dict(os.environ, {'area': area_json})
    assert load_area_json() == json.loads(area_json)
