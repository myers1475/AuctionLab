from __future__ import annotations

from dataclasses import dataclass

from auctionlab.observation.swing import Swing


@dataclass(frozen=True)
class MarketStructure:
    swing_high: Swing | None
    swing_low: Swing | None