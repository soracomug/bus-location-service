from lambdasrc.lpoint import LPoint

import pytest

def test_LPoint_latがfloatでないならValueErrorを返す():
    with pytest.raises(ValueError):
        LPoint('abcd',34.40094244423058)

def test_LPoint_lonがfloatでないならValueErrorを返す():
    with pytest.raises(ValueError):
        LPoint(132.71309945650137,'abcd')