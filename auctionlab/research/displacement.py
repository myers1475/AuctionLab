from auctionlab.reality.candle import Candle


def body_ratio(candle: Candle) -> float:
    total_range = candle.high - candle.low

    if total_range == 0:
        return 0.0

    body = abs(candle.close - candle.open)

    return body / total_range


def is_displacement(
    candle: Candle,
    minimum_ratio: float = 0.65,
) -> bool:
    return body_ratio(candle) >= minimum_ratio