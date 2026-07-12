from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from auctionlab.upo.upo import UPOStatus


@dataclass(frozen=True)
class InversionFairValueGap:
    created: datetime

    high: float
    low: float

    bullish: bool

    status: UPOStatus