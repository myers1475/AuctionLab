from datetime import datetime

from auctionlab.reality.candle import Candle


def test_bullish_candle():
    candle = Candle(
        timestamp=datetime(2025, 1, 1),
        open=100,
        high=111,
        low=99,
        close=110,
        volume=1000,
    )

    assert candle.bullish
    assert not candle.bearish
    assert candle.body == 10
    assert candle.range == 12
    assert candle.upper_wick == 1
    assert candle.lower_wick == 1


def test_bearish_candle():
    candle = Candle(
        timestamp=datetime(2025, 1, 1),
        open=110,
        high=111,
        low=99,
        close=100,
        volume=1000,
    )

    assert candle.bearish
    assert not candle.bullish