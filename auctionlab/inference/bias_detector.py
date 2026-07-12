from auctionlab.inference.control import Control
from auctionlab.inference.market_bias import MarketBias
from auctionlab.inference.objective_direction import ObjectiveDirection


def detect_bias(
    control: Control,
    direction: ObjectiveDirection,
) -> MarketBias:

    if (
        control == Control.BULLISH
        and direction == ObjectiveDirection.ABOVE
    ):
        return MarketBias.BULLISH

    if (
        control == Control.BEARISH
        and direction == ObjectiveDirection.BELOW
    ):
        return MarketBias.BEARISH

    return MarketBias.NEUTRAL