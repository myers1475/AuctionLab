from __future__ import annotations

from dataclasses import dataclass
from math import inf


@dataclass(frozen=True)
class Objective:
    kind: str
    price: float
    source: object


def nearest_objective(
    current_price: float,
    objectives: list[Objective],
) -> Objective | None:

    if not objectives:
        return None

    nearest = None
    nearest_distance = inf

    for objective in objectives:
        distance = abs(current_price - objective.price)

        if distance < nearest_distance:
            nearest_distance = distance
            nearest = objective

    return nearest