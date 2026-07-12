from auctionlab.observation.trading_day import TradingDay
from auctionlab.upo.previous_day import PreviousDay
from auctionlab.upo.upo import UPOStatus


def previous_day_levels(
    previous: TradingDay,
    current: TradingDay,
) -> PreviousDay:
    status = UPOStatus.ACTIVE

    if current.high > previous.high or current.low < previous.low:
        status = UPOStatus.COMPLETED

    return PreviousDay(
        high=previous.high,
        low=previous.low,
        status=status,
    )