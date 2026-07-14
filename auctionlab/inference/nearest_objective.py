from __future__ import annotations

from dataclasses import dataclass
from math import inf


@dataclass(frozen=True)
class Objective:
    kind: str
    price: float
    source: object

    @property
    def distance(self) -> float:
        return getattr(self, "_distance", 0.0)


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
            nearest = Objective(
                kind=objective.kind,
                price=objective.price,
                source=objective.source,
            )
            object.__setattr__(nearest, "_distance", distance)

    return nearest