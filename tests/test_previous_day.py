from datetime import datetime

from auctionlab.observation.trading_day import TradingDay
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle
from auctionlab.upo.previous_day_builder import previous_day_levels
from auctionlab.upo.upo import UPOStatus


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


def test_previous_day_active():
    previous = make_day(100, 80)
    current = make_day(95, 85)

    levels = previous_day_levels(previous, current)

    assert levels.status == UPOStatus.ACTIVE


def test_previous_day_completed():
    previous = make_day(100, 80)
    current = make_day(101, 85)

    levels = previous_day_levels(previous, current)

    assert levels.status == UPOStatus.COMPLETED