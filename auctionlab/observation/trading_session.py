from __future__ import annotations

from dataclasses import dataclass

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