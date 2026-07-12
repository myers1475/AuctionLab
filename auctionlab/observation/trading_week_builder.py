from datetime import date

from auctionlab.observation.trading_day import TradingDay
from auctionlab.observation.trading_week import TradingWeek


def _week_number(value) -> int:
    if isinstance(value, str):
        return date.fromisoformat(value).isocalendar().week

    return value.isocalendar().week


def build_trading_weeks(
    days: list[TradingDay],
) -> list[TradingWeek]:

    weeks: list[TradingWeek] = []

    current: list[TradingDay] = []

    current_week = None

    for day in days:

        week = _week_number(day.date)

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