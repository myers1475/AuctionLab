from __future__ import annotations

from dataclasses import dataclass

from auctionlab.research.direction import Direction
from auctionlab.research.target_type import TargetType


@dataclass(frozen=True)
class ResearchTarget:
    direction: Direction
    target_type: TargetType
    price: float