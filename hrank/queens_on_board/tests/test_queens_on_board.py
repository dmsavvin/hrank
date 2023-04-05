import pytest
import hrank.queens_on_board.tests.test_suits as ts
import hrank.queens_on_board.queens_on_board as qb


@pytest.mark.parametrize("test_input,expected", ts.QUEENS_ON_BOARD_TS)
def test_queens_on_board(test_input, expected):
    board = test_input
    assert qb.queensBoard(board) == expected
