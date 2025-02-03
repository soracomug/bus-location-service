from lambdasrc.lambda_function import lambda_handler
from lambdasrc.lpoint import LPoint
import os
from pytest_mock import MockFixture

import pytest
from lambdasrc.lambda_function import lambda_handler

@pytest.mark.parametrize("within_area_result, expected", [
    (True, {'within_area': True}),
    (False, {'within_area': False}),
])
def test_lambda_handler_within_areaの結果をJSONに整形して返す(within_area_result, expected, mocker):
    mocker.patch('lambdasrc.lambda_function.event_map_to_point', return_value={})
    mocker.patch('lambdasrc.lambda_function.load_area_json', return_value={})
    mocker.patch('lambdasrc.lambda_function.within_area', return_value=within_area_result)

    assert lambda_handler({}, None) == expected
