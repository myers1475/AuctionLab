from __future__ import annotations

from collections.abc import Iterator

from auctionlab.reality.candle import Candle


class BarSeries:
    def __init__(self, bars: list[Candle]):
        self._bars = tuple(bars)

    def __len__(self) -> int:
        return len(self._bars)

    def __getitem__(self, index: int) -> Candle:
        return self._bars[index]

    def __iter__(self) -> Iterator[Candle]:
        return iter(self._bars)

    @property
    def first(self) -> Candle:
        return self._bars[0]

    @property
    def last(self) -> Candle:
        return self._bars[-1]

    @property
    def highs(self) -> list[float]:
        return [bar.high for bar in self._bars]

    @property
    def lows(self) -> list[float]:
        return [bar.low for bar in self._bars]

    @property
    def opens(self) -> list[float]:
        return [bar.open for bar in self._bars]

    @property
    def closes(self) -> list[float]:
        return [bar.close for bar in self._bars]