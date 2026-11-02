import time

import pytest


@pytest.mark.parametrize("n", range(1, 21))
def test_imitation_of_slow_check(n):
    time.sleep(1)
    assert n > 0
