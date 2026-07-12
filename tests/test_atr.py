from datetime import datetime, timedelta

from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle
from auctionlab.research.atr import atr14


def make_bar(i: int) -> Candle:
    return Candle(
        timestamp=datetime(2026, 1, 1) + timedelta(minutes=i * 5),
        open=100,
        high=110,
        low=100,
        close=105,
    )


def test_atr14():

    bars = BarSeries(
        [make_bar(i) for i in range(20)]
    )

    values = atr14(bars)

    assert len(values) == 20
    assert values[0] is None
    assert values[12] is None
    assert values[13] == 10