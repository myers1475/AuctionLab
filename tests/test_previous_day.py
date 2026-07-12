from datetime import datetime

from auctionlab.observation.trading_day import TradingDay
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle
from auctionlab.upo.previous_day_builder import previous_day_levels


def make_day(high: float, low: float) -> TradingDay:
    bars = BarSeries(
        [
            Candle(
                timestamp=datetime.now(),
                open=1,
                high=high,
                low=low,
                close=1,
            )
        ]
    )

    return TradingDay(
        date="2026-01-01",
        bars=bars,
    )


def test_previous_day_levels():
    previous = make_day(100, 85)

    levels = previous_day_levels(previous)

    assert levels.high == 100
    assert levels.low == 85