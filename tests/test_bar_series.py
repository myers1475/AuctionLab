from datetime import datetime

from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def make_bar(price: float) -> Candle:
    return Candle(
        timestamp=datetime.now(),
        open=price,
        high=price + 1,
        low=price - 1,
        close=price,
    )


def test_bar_series_length():
    bars = BarSeries([make_bar(1), make_bar(2)])

    assert len(bars) == 2


def test_bar_series_indexing():
    bars = BarSeries([make_bar(1), make_bar(2)])

    assert bars[0].open == 1
    assert bars[1].open == 2


def test_first():
    bars = BarSeries([make_bar(1), make_bar(2)])

    assert bars.first.open == 1


def test_last():
    bars = BarSeries([make_bar(1), make_bar(2)])

    assert bars.last.open == 2


def test_highs():
    bars = BarSeries([make_bar(1), make_bar(2)])

    assert bars.highs == [2, 3]


def test_lows():
    bars = BarSeries([make_bar(1), make_bar(2)])

    assert bars.lows == [0, 1]