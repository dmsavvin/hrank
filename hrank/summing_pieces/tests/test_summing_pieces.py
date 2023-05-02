import pytest
import hrank.summing_pieces.tests.test_suits as ts
import hrank.summing_pieces.summing_pieces as sp


@pytest.mark.parametrize("test_input,expected", ts.SUMMING_PIECES_TS)
def test_two_subsequence(test_input, expected):
    arr = test_input
    assert sp.summing_pieces(arr) == expected
