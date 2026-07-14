from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective


@dataclass(frozen=True)
class Observation:
    timestamp: datetime

    current_price: float

    visible_objectives: tuple[Objective, ...]

    nearest_objective: Objective | None

    control: Control

    @property
    def distance_to_target(self) -> float | None:

        if self.nearest_objective is None:
            return None

        return self.nearest_objective.distance