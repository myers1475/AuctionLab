from dataclasses import dataclass


@dataclass(frozen=True)
class ObjectiveContext:
    current_price: float
    upside_objective: object | None
    downside_objective: object | None