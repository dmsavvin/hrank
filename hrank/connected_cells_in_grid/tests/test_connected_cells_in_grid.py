import pytest
import hrank.connected_cells_in_grid.tests.test_suits as ts
import hrank.connected_cells_in_grid.connected_cells_in_grid as cs


@pytest.mark.parametrize("test_input,expected", ts.CONNECTED_CELLS_TS)
def test_connected_cells_in_grid(test_input, expected):
    matrix = test_input
    assert cs.connected_cells_in_grid(matrix) == expected
