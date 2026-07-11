from datetime import datetime

from auctionlab.observation.trading_session import TradingSession
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle
from auctionlab.upo.session_levels_detector import detect_session_levels


def test_session_levels():
    bars = BarSeries(
        [
            Candle(datetime(2026, 1, 1, 20, 0), 1, 10, 5, 1),
            Candle(datetime(2026, 1, 1, 20, 5), 1, 15, 4, 1),
            Candle(datetime(2026, 1, 1, 20, 10), 1, 12, 6, 1),
        ]
    )

    session = TradingSession(
        name="Asia",
        bars=bars,
    )

    levels = detect_session_levels(session)

    assert levels.session == "Asia"
    assert levels.high == 15
    assert levels.low == 4