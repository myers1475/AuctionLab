from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def load_csv(path: str | Path) -> BarSeries:
    """
    Load TradingView OHLC CSV data into a BarSeries.
    """

    candles: list[Candle] = []

    with open(path, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            candles.append(
                Candle(
                    timestamp=datetime.fromtimestamp(int(row["time"])),
                    open=float(row["open"]),
                    high=float(row["high"]),
                    low=float(row["low"]),
                    close=float(row["close"]),
                    volume=None,
                )
            )

    return BarSeries(candles)