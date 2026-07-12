from datetime import datetime

from auctionlab.reality.candle import Candle
from auctionlab.research.direction import Direction
from auctionlab.research.excursion import mae, mfe


def test_long_excursion():

    candle = Candle(
        timestamp=datetime.now(),
        open=100,
        high=108,
        low=97,
        close=105,
    )

    assert mae(100, candle, Direction.LONG) == 3
    assert mfe(100, candle, Direction.LONG) == 8


def test_short_excursion():

    candle = Candle(
        timestamp=datetime.now(),
        open=100,
        high=104,
        low=92,
        close=95,
    )

    assert mae(100, candle, Direction.SHORT) == 4
    assert mfe(100, candle, Direction.SHORT) == 8