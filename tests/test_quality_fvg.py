from datetime import datetime, timedelta

from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle
from auctionlab.research.quality_fvg import detect_quality_bullish_fvgs


def bar(minutes, open_, high, low, close):
    return Candle(
        timestamp=datetime(2026, 1, 1) + timedelta(minutes=minutes),
        open=open_,
        high=high,
        low=low,
        close=close,
    )


def test_quality_fvg():
    bars = BarSeries(
        [
            bar(0, 95, 100, 95, 99),
            bar(5, 99, 110, 98, 109),
            bar(10, 109, 115, 105, 114),
        ]
    )

    fvgs = detect_quality_bullish_fvgs(
        bars,
        minimum_gap=3,
        minimum_body_ratio=0.6,
    )

    assert len(fvgs) == 1