from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from auctionlab.core.event import Event
from auctionlab.reality.candle import Candle


@dataclass(frozen=True)
class Swing(Event):
    candle: Candle
    index: int
    is_high: bool