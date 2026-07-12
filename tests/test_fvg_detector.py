from datetime import datetime, timedelta

from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle
from auctionlab.upo.fvg_detector import detect_bullish_fvgs
from auctionlab.upo.upo import UPOStatus


def bar(minutes, high, low):
    return Candle(
        timestamp=datetime(2026, 1, 1) + timedelta(minutes=minutes),
        open=0,
        high=high,
        low=low,
        close=0,
    )


def test_active_bullish_fvgs():
    bars = BarSeries(
        [
            bar(0, 100, 95),
            bar(5, 103, 98),
            bar(10, 110, 105),
            bar(15, 111, 106),
        ]
    )

    fvgs = detect_bullish_fvgs(bars)

    assert len(fvgs) == 2

    assert fvgs[0].status == UPOStatus.ACTIVE
    assert fvgs[0].completed is None

    assert fvgs[1].status == UPOStatus.ACTIVE
    assert fvgs[1].completed is None


def test_completed_bullish_fvgs():
    bars = BarSeries(
        [
            bar(0, 100, 95),
            bar(5, 103, 98),
            bar(10, 110, 105),
            bar(15, 111, 106),
            bar(20, 108, 99),
        ]
    )

    fvgs = detect_bullish_fvgs(bars)

    assert len(fvgs) == 2

    assert fvgs[0].status == UPOStatus.COMPLETED
    assert fvgs[0].completed is not None

    assert fvgs[1].status == UPOStatus.COMPLETED
    assert fvgs[1].completed is not None