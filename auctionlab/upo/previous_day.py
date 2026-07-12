from __future__ import annotations

from dataclasses import dataclass

from auctionlab.upo.upo import UPOStatus


@dataclass(frozen=True)
class PreviousDay:
    high: float
    low: float
    status: UPOStatus