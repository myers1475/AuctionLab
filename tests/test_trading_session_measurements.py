from datetime import datetime, timedelta

from auctionlab.observation.trading_session import TradingSession
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def bar(minutes, open_, high, low, close):
    return Candle(
        timestamp=datetime(2026, 1, 1, 20, 0) + timedelta(minutes=minutes),
        open=open_,
        high=high,
        low=low,
        close=close,
    )


def test_session_measurements():
    session = TradingSession(
        name="Asia",
        bars=BarSeries(
            [
                bar(0, 100, 101, 99, 100),
                bar(5, 100, 105, 98, 103),
                bar(10, 103, 104, 97, 99),
            ]
        ),
    )

    assert session.open == 100
    assert session.close == 99
    assert session.high == 105
    assert session.low == 97
    assert session.range == 8