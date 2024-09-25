import lambdasrc.lambda_function
import pytest

def test_LPoint_latがfloatでないならValueErrorを返す():
    with pytest.raises(ValueError):
        lambdasrc.lambda_function.LPoint('abcd',34.40094244423058)

def test_LPoint_lonがfloatでないならValueErrorを返す():
    with pytest.raises(ValueError):
        lambdasrc.lambda_function.LPoint(132.71309945650137,'abcd')