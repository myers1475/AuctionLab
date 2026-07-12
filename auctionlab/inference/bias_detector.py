from auctionlab.inference.control import Control
from auctionlab.inference.market_bias import MarketBias
from auctionlab.inference.nearest_objective import Objective


def detect_bias(
    control: Control,
    nearest: Objective | None,
) -> MarketBias:

    if nearest is None:
        return MarketBias.NEUTRAL

    if control == Control.BULLISH and "Low" in nearest.kind:
        return MarketBias.BULLISH

    if control == Control.BEARISH and "High" in nearest.kind:
        return MarketBias.BEARISH

    return MarketBias.NEUTRAL