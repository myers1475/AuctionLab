from __future__ import annotations

from dataclasses import dataclass

from auctionlab.reality.candle import Candle


@dataclass(frozen=True)
class Swing:
    candle: Candle
    index: int
    is_high: bool