from auctionlab.inference.nearest_objective import (
    Objective,
    nearest_objective,
)

from auctionlab.research.experiments.observation import Observation


def run(
    *,
    timestamp,
    current_price: float,
    objectives: list[Objective],
):

    objective = nearest_objective(
        current_price=current_price,
        objectives=objectives,
    )

    if objective is None:
        return None

    return Observation(
        timestamp=timestamp,
        current_price=current_price,
        objective_kind=objective.kind,
        objective_price=objective.price,
        source=objective.source,
    )