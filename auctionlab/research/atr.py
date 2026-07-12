from __future__ import annotations

from auctionlab.reality.bar_series import BarSeries


def atr(
    bars: BarSeries,
    period: int = 14,
) -> list[float | None]:
    if len(bars) == 0:
        return []

    true_ranges: list[float] = []

    for i, bar in enumerate(bars):
        if i == 0:
            true_ranges.append(bar.high - bar.low)
        else:
            previous_close = bars[i - 1].close

            true_ranges.append(
                max(
                    bar.high - bar.low,
                    abs(bar.high - previous_close),
                    abs(bar.low - previous_close),
                )
            )

    values: list[float | None] = [None] * len(bars)

    if len(bars) < period:
        return values

    running_sum = sum(true_ranges[:period])

    values[period - 1] = running_sum / period

    for i in range(period, len(true_ranges)):
        running_sum += true_ranges[i]
        running_sum -= true_ranges[i - period]
        values[i] = running_sum / period

    return values


def atr14(bars: BarSeries) -> list[float | None]:
    return atr(bars, 14)