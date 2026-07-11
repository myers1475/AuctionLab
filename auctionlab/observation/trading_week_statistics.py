from auctionlab.observation.trading_week import TradingWeek


def week_high(week: TradingWeek) -> float:
    return max(day.high for day in week.days)


def week_low(week: TradingWeek) -> float:
    return min(day.low for day in week.days)