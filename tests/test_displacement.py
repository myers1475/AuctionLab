from datetime import datetime

from auctionlab.research.displacement import (
    body_ratio,
    is_displacement,
)
from auctionlab.reality.candle import Candle


def test_body_ratio():
    candle = Candle(
        timestamp=datetime.now(),
        open=100,
        high=110,
        low=90,
        close=108,
    )

    assert body_ratio(candle) == 8 / 20


def test_displacement_true():
    candle = Candle(
        timestamp=datetime.now(),
        open=100,
        high=110,
        low=99,
        close=109,
    )

    assert is_displacement(candle, 0.6)


def test_displacement_false():
    candle = Candle(
        timestamp=datetime.now(),
        open=100,
        high=110,
        low=90,
        close=102,
    )

    assert not is_displacement(candle, 0.6)