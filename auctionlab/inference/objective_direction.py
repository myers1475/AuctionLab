from __future__ import annotations

from enum import Enum

from auctionlab.inference.nearest_objective import Objective


class ObjectiveDirection(Enum):
    ABOVE = "Above"
    BELOW = "Below"
    AT = "At"


def objective_direction(
    current_price: float,
    objective: Objective,
) -> ObjectiveDirection:

    if objective.price > current_price:
        return ObjectiveDirection.ABOVE

    if objective.price < current_price:
        return ObjectiveDirection.BELOW

    return ObjectiveDirection.AT