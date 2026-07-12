from auctionlab.reality.candle import Candle
from auctionlab.research.active_hypothesis_manager import (
    ActiveHypothesisManager,
)
from auctionlab.research.active_hypothesis_updater import advance
from auctionlab.research.direction import Direction


def advance_all(
    manager: ActiveHypothesisManager,
    candle: Candle,
    direction: Direction,
) -> None:

    for hypothesis in manager.active:
        advance(
            hypothesis,
            candle,
            direction,
        )