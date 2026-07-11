from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta

from auctionlab.reality.bar_series import BarSeries


@dataclass(frozen=True)
class TradingSession:
    name: str
    bars: BarSeries

    @property
    def high(self) -> float:
        return max(bar.high for bar in self.bars)

    @property
    def low(self) -> float:
        return min(bar.low for bar in self.bars)

    @property
    def initial_balance(self) -> BarSeries:
        start = self.bars.first.timestamp

        return BarSeries(
            [
                bar
                for bar in self.bars
                if bar.timestamp < start + timedelta(hours=1)
            ]
        )

    @property
    def ib_high(self) -> float:
        return max(bar.high for bar in self.initial_balance)

    @property
    def ib_low(self) -> float:
        return min(bar.low for bar in self.initial_balance)