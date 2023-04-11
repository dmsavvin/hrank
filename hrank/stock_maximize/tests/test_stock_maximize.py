import pytest
import hrank.stock_maximize.tests.test_suits as ts
import hrank.stock_maximize.stock_maximize as sm


@pytest.mark.parametrize("test_input,expected", ts.STOCK_MAXIMIZE_TS)
def test_stock_maximize(test_input, expected):
    prices = test_input
    assert sm.stockmax(prices) == expected
