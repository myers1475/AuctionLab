from auctionlab.reality.candle import Candle

from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import (
    Objective,
    nearest_objective,
)
from auctionlab.observation.market_snapshot import MarketSnapshot


def build_snapshot(
    *,
    timestamp,
    candle: Candle,
    current_price: float,
    objectives: list[Objective],
    active_upos: ActiveUPOs,
    control: Control,
) -> MarketSnapshot:

    return MarketSnapshot(
        timestamp=timestamp,
        candle=candle,
        current_price=current_price,
        active_upos=active_upos,
        control=control,
        nearest_objective=nearest_objective(
            current_price,
            objectives,
        ),
    )