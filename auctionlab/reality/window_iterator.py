from __future__ import annotations

from collections.abc import Iterator

from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.bar_window import BarWindow


def windows(bars: BarSeries) -> Iterator[BarWindow]:
    for i in range(1, len(bars) - 1):
        yield BarWindow(
            previous=bars[i - 1],
            current=bars[i],
            next=bars[i + 1],
        )