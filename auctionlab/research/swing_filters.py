from auctionlab.observation.swing import Swing


def minimum_move(
    swings: list[Swing],
    minimum: float,
) -> list[Swing]:

    if not swings:
        return []

    filtered = [swings[0]]

    for swing in swings[1:]:

        previous = filtered[-1]

        previous_price = (
            previous.candle.high
            if previous.is_high
            else previous.candle.low
        )

        current_price = (
            swing.candle.high
            if swing.is_high
            else swing.candle.low
        )

        if abs(current_price - previous_price) >= minimum:
            filtered.append(swing)

    return filtered