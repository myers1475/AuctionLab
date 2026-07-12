from auctionlab.reality.candle import Candle
from auctionlab.research.direction import Direction


def mae(
    entry_price: float,
    candle: Candle,
    direction: Direction,
) -> float:

    if direction == Direction.LONG:
        return max(0.0, entry_price - candle.low)

    return max(0.0, candle.high - entry_price)


def mfe(
    entry_price: float,
    candle: Candle,
    direction: Direction,
) -> float:

    if direction == Direction.LONG:
        return max(0.0, candle.high - entry_price)

    return max(0.0, entry_price - candle.low)