from auctionlab.observation.trading_week import TradingWeek
from auctionlab.observation.trading_week_statistics import (
    week_high,
    week_low,
)
from auctionlab.upo.previous_week import PreviousWeek


def previous_week_levels(
    week: TradingWeek,
) -> PreviousWeek:
    return PreviousWeek(
        high=week_high(week),
        low=week_low(week),
    )