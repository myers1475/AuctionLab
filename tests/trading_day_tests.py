from datetime import datetime

from auctionlab.observation.trading_day_builder import build_trading_days
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def test_build_trading_day():
    bars = BarSeries(
        [
            Candle(datetime(2026, 1, 1, 18, 0), 1, 2, 0, 1.5),
            Candle(datetime(2026, 1, 1, 18, 5), 2, 3, 1, 2.5),
            Candle(datetime(2026, 1, 2, 17, 55), 3, 4, 2, 3.5),
        ]
    )

    days = build_trading_days(bars)

    assert len(days) == 1
    assert days[0].open == 1
    assert days[0].high == 4
    assert days[0].low == 0
    assert days[0].close == 3.5