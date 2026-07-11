from datetime import datetime, timedelta

from auctionlab.observation.trading_session import TradingSession
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def make_bar(minutes: int, high: float, low: float):
    return Candle(
        timestamp=datetime(2026, 1, 1, 20, 0) + timedelta(minutes=minutes),
        open=1,
        high=high,
        low=low,
        close=1,
    )


def test_initial_balance():
    bars = BarSeries(
        [
            make_bar(0, 10, 5),
            make_bar(5, 12, 6),
            make_bar(55, 15, 4),
            make_bar(60, 20, 1),
        ]
    )

    session = TradingSession(
        name="Asia",
        bars=bars,
    )

    assert session.ib_high == 15
    assert session.ib_low == 4