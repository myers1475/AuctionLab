from auctionlab.observation.trading_day import TradingDay
from auctionlab.observation.trading_week import TradingWeek
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle
from auctionlab.upo.previous_week_builder import previous_week_levels


def make_day(day, high, low):

    bar = Candle(
        timestamp=None,
        open=100,
        high=high,
        low=low,
        close=100,
    )

    return TradingDay(
        date=f"2025-12-{day:02d}",
        bars=BarSeries([bar]),
    )


def test_previous_week_levels():

    week = TradingWeek(
        days=(
            make_day(15, 100, 90),
            make_day(16, 110, 95),
            make_day(17, 105, 85),
        )
    )

    previous = previous_week_levels(week)

    assert previous.high == 110
    assert previous.low == 85