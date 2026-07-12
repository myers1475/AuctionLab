from datetime import date

from auctionlab.observation.trading_day import TradingDay
from auctionlab.observation.trading_week_builder import (
    build_trading_weeks,
)


def make_day(year, month, day):

    return TradingDay(
        date=date(year, month, day),
        bars=(),
    )


def test_build_weeks():

    days = [
        make_day(2025, 12, 15),
        make_day(2025, 12, 16),
        make_day(2025, 12, 17),
        make_day(2025, 12, 18),
        make_day(2025, 12, 19),
        make_day(2025, 12, 22),
    ]

    weeks = build_trading_weeks(days)

    assert len(weeks) == 2
    assert len(weeks[0].days) == 5
    assert len(weeks[1].days) == 1