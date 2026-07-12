from auctionlab.inference.nearest_objective import Objective
from auctionlab.inference.objective_direction import (
    ObjectiveDirection,
    objective_direction,
)


def test_objective_above():
    direction = objective_direction(
        100,
        Objective(
            kind="PDH",
            price=110,
            source=None,
        ),
    )

    assert direction == ObjectiveDirection.ABOVE


def test_objective_below():
    direction = objective_direction(
        100,
        Objective(
            kind="PDL",
            price=90,
            source=None,
        ),
    )

    assert direction == ObjectiveDirection.BELOW


def test_objective_at():
    direction = objective_direction(
        100,
        Objective(
            kind="PDH",
            price=100,
            source=None,
        ),
    )

    assert direction == ObjectiveDirection.AT