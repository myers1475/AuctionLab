from __future__ import annotations

from collections.abc import Iterator

from auctionlab.reality.candle import Candle


class BarSeries:
    """
    Immutable ordered collection of candles.
    """

    def __init__(self, candles: list[Candle]):
        self._candles = tuple(candles)

    def __len__(self) -> int:
        return len(self._candles)

    def __getitem__(self, index: int) -> Candle:
        return self._candles[index]

    def __iter__(self) -> Iterator[Candle]:
        return iter(self._candles)