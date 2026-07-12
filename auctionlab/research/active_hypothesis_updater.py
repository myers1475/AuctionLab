from auctionlab.reality.candle import Candle
from auctionlab.research.active_hypothesis import ActiveHypothesis
from auctionlab.research.excursion import mae, mfe
from auctionlab.research.direction import Direction


def advance(
    active: ActiveHypothesis,
    candle: Candle,
    direction: Direction,
) -> ActiveHypothesis:

    active.bars_elapsed += 1

    active.mae = max(
        active.mae,
        mae(
            active.entry_price,
            candle,
            direction,
        ),
    )

    active.mfe = max(
        active.mfe,
        mfe(
            active.entry_price,
            candle,
            direction,
        ),
    )

    return active