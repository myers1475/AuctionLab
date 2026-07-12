from datetime import datetime, timedelta

from auctionlab.observation.swing_detector import detect_swings
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def make_bar(i, high, low):
    return Candle(
        timestamp=datetime(2026, 1, 1) + timedelta(minutes=5 * i),
        open=(high + low) / 2,
        high=high,
        low=low,
        close=(high + low) / 2,
    )


def test_detects_one_swing_high():

    bars = BarSeries(
        [
            make_bar(0, 10, 5),
            make_bar(1, 11, 5),
            make_bar(2, 15, 5),
            make_bar(3, 11, 5),
            make_bar(4, 10, 5),
        ]
    )

    swings = detect_swings(bars)

    assert len(swings) == 1
    assert swings[0].is_high


def test_detects_one_swing_low():

    bars = BarSeries(
        [
            make_bar(0, 10, 10),
            make_bar(1, 10, 9),
            make_bar(2, 10, 5),
            make_bar(3, 10, 9),
            make_bar(4, 10, 10),
        ]
    )

    swings = detect_swings(bars)

    assert len(swings) == 1
    assert not swings[0].is_high