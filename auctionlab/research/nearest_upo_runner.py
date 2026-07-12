from auctionlab.reality.bar_series import BarSeries


def target_reached(
    bars: BarSeries,
    start_index: int,
    target_price: float,
) -> bool:

    for bar in bars[start_index + 1:]:

        if bar.high >= target_price:
            return True

    return False