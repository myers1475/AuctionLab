from datetime import time

from auctionlab.observation.trading_day import TradingDay
from auctionlab.observation.trading_session import TradingSession
from auctionlab.reality.bar_series import BarSeries


def session(
    day: TradingDay,
    name: str,
    start: time,
    end: time,
) -> TradingSession:
    bars = [
        bar
        for bar in day.bars
        if start <= bar.timestamp.time() <= end
    ]

    return TradingSession(
        name=name,
        bars=BarSeries(bars),
    )