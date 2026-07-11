from auctionlab.upo.previous_week import PreviousWeek


def build_previous_week(high: float, low: float) -> PreviousWeek:
    return PreviousWeek(
        high=high,
        low=low,
    )