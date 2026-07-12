from __future__ import annotations

from dataclasses import dataclass

from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective


@dataclass(frozen=True)
class MarketSnapshot:
    current_price: float

    active_upos: ActiveUPOs
    control: Control

    nearest_objective: Objective | None