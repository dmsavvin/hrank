import pytest
import hrank.string_reduction.tests.test_suits as ts
import hrank.string_reduction.string_reduction as sr


@pytest.mark.parametrize("test_input,expected", ts.STRING_REDUCTION_TS)
def test_string_reduction(test_input, expected):
    s = test_input
    assert sr.string_reduction(s) == expected
