from __future__ import annotations

from collections import defaultdict
from datetime import timedelta

from auctionlab.observation.trading_day import TradingDay
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def build_trading_days(bars: BarSeries) -> list[TradingDay]:
    grouped: dict[str, list[Candle]] = defaultdict(list)

    for bar in bars:
        trading_date = bar.timestamp

        if trading_date.hour >= 18:
            trading_date = trading_date + timedelta(days=1)

        key = trading_date.strftime("%Y-%m-%d")

        grouped[key].append(bar)

    return [
        TradingDay(
            date=day,
            bars=BarSeries(day_bars),
        )
        for day, day_bars in sorted(grouped.items())
    ]