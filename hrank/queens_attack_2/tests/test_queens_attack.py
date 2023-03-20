import pytest
import hrank.queens_attack_2.tests.test_suits as ts
import hrank.queens_attack_2.queens_attack as qa


@pytest.mark.parametrize("test_input,expected", ts.QUEENS_ATTACK_TS)
def test_queens_attack(test_input, expected):
    n, k, r_q, c_q, obstacles = test_input
    assert qa.queens_attack(n, k, r_q, c_q, obstacles) == expected
