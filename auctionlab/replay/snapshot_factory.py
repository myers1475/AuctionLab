from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import (
    Objective,
    nearest_objective,
)
from auctionlab.observation.market_snapshot import MarketSnapshot


def build_snapshot(
    *,
    current_price: float,
    objectives: list[Objective],
    active_upos: ActiveUPOs,
    control: Control,
) -> MarketSnapshot:

    return MarketSnapshot(
        current_price=current_price,
        active_upos=active_upos,
        control=control,
        nearest_objective=nearest_objective(
            current_price,
            objectives,
        ),
    )