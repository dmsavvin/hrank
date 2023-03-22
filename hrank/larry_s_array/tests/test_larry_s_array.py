import pytest
import hrank.larry_s_array.tests.test_suits as ts
import hrank.larry_s_array.larry_s_array as la


@pytest.mark.parametrize("test_input,expected", ts.LARRY_S_ARRAY_TS)
def test_larry_s_array(test_input, expected):
    A = test_input
    assert la.larry_s_array(A) == expected
