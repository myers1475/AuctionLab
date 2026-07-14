from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from auctionlab.reality.candle import Candle
from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective


@dataclass(frozen=True)
class MarketSnapshot:
    timestamp: datetime

    candle: Candle

    current_price: float

    active_upos: ActiveUPOs
    control: Control

    nearest_objective: Objective | None