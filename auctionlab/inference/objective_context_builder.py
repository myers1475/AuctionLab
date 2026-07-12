from auctionlab.inference.nearest_directional_upo import (
    nearest_downside_upo,
    nearest_upside_upo,
)
from auctionlab.inference.objective_context import ObjectiveContext
from auctionlab.inference.upo_repository import UPORepository


def build_objective_context(
    current_price: float,
    repository: UPORepository,
) -> ObjectiveContext:

    return ObjectiveContext(
        current_price=current_price,
        upside_objective=nearest_upside_upo(
            current_price,
            repository,
        ),
        downside_objective=nearest_downside_upo(
            current_price,
            repository,
        ),
    )