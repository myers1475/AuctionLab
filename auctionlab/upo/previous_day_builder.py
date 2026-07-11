from auctionlab.observation.trading_day import TradingDay
from auctionlab.upo.previous_day import PreviousDay


def build_previous_day(previous: TradingDay) -> PreviousDay:
    return PreviousDay(
        created=previous.bars.last.timestamp,
        high=previous.high,
        low=previous.low,
    )