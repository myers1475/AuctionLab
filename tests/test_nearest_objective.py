from auctionlab.inference.nearest_objective import (
    Objective,
    nearest_objective,
)


def test_nearest_objective():

    objectives = [
        Objective("PDH", 100, None),
        Objective("Swing High", 110, None),
        Objective("FVG", 125, None),
    ]

    nearest = nearest_objective(
        current_price=108,
        objectives=objectives,
    )

    assert nearest is not None
    assert nearest.kind == "Swing High"
    assert nearest.price == 110
    assert nearest.distance == 2