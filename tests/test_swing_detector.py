from datetime import datetime, timedelta

from auctionlab.observation.swing_detector import detect_swings
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def make_bar(i, high=10, low=5):
    return Candle(
        timestamp=datetime(2026, 1, 1) + timedelta(minutes=5 * i),
        open=(high + low) / 2,
        high=high,
        low=low,
        close=(high + low) / 2,
    )


def test_detects_one_swing_high():

    bars = []

    # Build enough history for ATR(14)
    for i in range(20):
        bars.append(make_bar(i))

    # Create a valid N=2 swing high at index 15
    bars[13] = make_bar(13, high=11)
    bars[14] = make_bar(14, high=12)
    bars[15] = make_bar(15, high=20)
    bars[16] = make_bar(16, high=12)
    bars[17] = make_bar(17, high=11)

    swings = detect_swings(BarSeries(bars))

    highs = [s for s in swings if s.is_high]

    assert len(highs) == 1
    assert highs[0].index == 15


def test_detects_one_swing_low():

    bars = []

    for i in range(20):
        bars.append(make_bar(i))

    bars[13] = make_bar(13, low=9)
    bars[14] = make_bar(14, low=8)
    bars[15] = make_bar(15, low=1)
    bars[16] = make_bar(16, low=8)
    bars[17] = make_bar(17, low=9)

    swings = detect_swings(BarSeries(bars))

    lows = [s for s in swings if not s.is_high]

    assert len(lows) == 1
    assert lows[0].index == 15