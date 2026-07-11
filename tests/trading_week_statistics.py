from datetime import datetime

from auctionlab.observation.trading_day import TradingDay
from auctionlab.observation.trading_week import TradingWeek
from auctionlab.observation.trading_week_statistics import (
    week_high,
    week_low,
)
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def make_day(high: float, low: float) -> TradingDay:
    return TradingDay(
        date="2026-01-01",
        bars=BarSeries(
            [
                Candle(
                    timestamp=datetime.now(),
                    open=1,
                    high=high,
                    low=low,
                    close=1,
                )
            ]
        ),
    )


def test_week_high_low():
    week = TradingWeek(
        start_date="2025-12-28",
        end_date="2026-01-02",
        days=(
            make_day(100, 90),
            make_day(105, 91),
            make_day(102, 88),
        ),
    )

    assert week_high(week) == 105
    assert week_low(week) == 88