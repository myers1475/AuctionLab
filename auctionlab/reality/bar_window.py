from __future__ import annotations

from dataclasses import dataclass

from auctionlab.reality.candle import Candle


@dataclass(frozen=True)
class BarWindow:
    previous: Candle
    current: Candle
    next: Candle