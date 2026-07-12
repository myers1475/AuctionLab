from auctionlab.observation.trading_day import TradingDay
from auctionlab.upo.previous_day import PreviousDay


def previous_day_levels(previous: TradingDay) -> PreviousDay:
    return PreviousDay(
        high=previous.high,
        low=previous.low,
    )