import pytest
import hrank.pairs.tests.test_suits as ts
import hrank.pairs.pairs as pr


@pytest.mark.parametrize("test_input,expected", ts.PAIRS_TS)
def test_pairs(test_input, expected):
    k, arr = test_input
    assert pr.pairs(k, arr) == expected
