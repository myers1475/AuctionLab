from auctionlab.observation.trading_day import TradingDay
from auctionlab.observation.trading_week import TradingWeek


def build_trading_weeks(
    days: list[TradingDay],
) -> list[TradingWeek]:

    weeks: list[TradingWeek] = []

    current: list[TradingDay] = []

    current_week = None

    for day in days:

        week = day.date.isocalendar().week

        if current_week is None:
            current_week = week

        if week != current_week:
            weeks.append(
                TradingWeek(days=tuple(current))
            )
            current = []
            current_week = week

        current.append(day)

    if current:
        weeks.append(
            TradingWeek(days=tuple(current))
        )

    return weeks