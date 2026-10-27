import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from margin import min_price, profit  # noqa: E402


def test_min_price_leaves_the_target_margin():
    price = min_price(20, 10, margin=0.20)
    net, margin = profit(price, 20, 10)
    assert margin == pytest.approx(0.20, abs=0.005) and net > 0


def test_profit_of_a_given_price():
    assert profit(100, 40, 15) == (33.5, 0.335)


def test_a_loss_is_negative():
    assert profit(30, 25, 10)[0] < 0


def test_invalid_inputs_are_rejected():
    with pytest.raises(ValueError):
        min_price(-1, 5)
    with pytest.raises(ValueError):
        min_price(10, 5, margin=0.95)
    with pytest.raises(ValueError):
        profit(0, 10, 5)
