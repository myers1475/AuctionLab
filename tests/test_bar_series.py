from datetime import datetime

from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def test_bar_series_length():
    candles = [
        Candle(datetime.now(), 1, 2, 0, 1.5, 100),
        Candle(datetime.now(), 2, 3, 1, 2.5, 100),
    ]

    bars = BarSeries(candles)

    assert len(bars) == 2


def test_bar_series_indexing():
    candles = [
        Candle(datetime.now(), 1, 2, 0, 1.5, 100),
        Candle(datetime.now(), 2, 3, 1, 2.5, 100),
    ]

    bars = BarSeries(candles)

    assert bars[0].open == 1
    assert bars[1].close == 2.5