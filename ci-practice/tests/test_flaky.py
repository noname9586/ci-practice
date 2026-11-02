import random

import pytest


@pytest.mark.quarantine
def test_unstable_response_time():
    # Имитация нестабильной проверки: иногда тест завершается ошибкой.
    assert random.random() > 0.33
