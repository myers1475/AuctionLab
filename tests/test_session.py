from datetime import datetime, time

from auctionlab.observation.session import session
from auctionlab.observation.trading_day import TradingDay
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def test_session():
    bars = BarSeries(
        [
            Candle(datetime(2026, 1, 1, 19, 55), 1, 2, 0, 1),
            Candle(datetime(2026, 1, 1, 20, 0), 1, 5, 0, 1),
            Candle(datetime(2026, 1, 1, 20, 5), 1, 7, 0, 1),
            Candle(datetime(2026, 1, 1, 23, 55), 1, 4, 0, 1),
        ]
    )

    day = TradingDay(
        date="2026-01-02",
        bars=bars,
    )

    asia = session(
        day,
        "Asia",
        time(20, 0),
        time(23, 59, 59),
    )

    assert asia.name == "Asia"
    assert len(asia.bars) == 3
    assert asia.high == 7
    assert asia.low == 0