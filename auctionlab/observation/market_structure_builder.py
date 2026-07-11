from auctionlab.observation.market_structure import MarketStructure
from auctionlab.observation.swing import Swing


def build_market_structure(swings: list[Swing]) -> MarketStructure:
    swing_high = None
    swing_low = None

    for swing in swings:
        if swing.is_high:
            swing_high = swing
        else:
            swing_low = swing

    return MarketStructure(
        swing_high=swing_high,
        swing_low=swing_low,
    )