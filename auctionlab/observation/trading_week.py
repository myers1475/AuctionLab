from __future__ import annotations

from dataclasses import dataclass

from auctionlab.observation.trading_day import TradingDay


@dataclass(frozen=True)
class TradingWeek:
    days: tuple[TradingDay, ...]