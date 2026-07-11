from datetime import datetime

from auctionlab.observation.swing_detector import detect_two_bar_swings
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def test_detects_one_swing_high():
    bars = BarSeries(
        [
            Candle(datetime.now(), 1, 2, 1, 2),
            Candle(datetime.now(), 2, 5, 2, 4),
            Candle(datetime.now(), 3, 3, 2, 2),
        ]
    )

    swings = detect_two_bar_swings(bars)

    assert len(swings) == 1
    assert swings[0].is_high


def test_detects_one_swing_low():
    bars = BarSeries(
        [
            Candle(datetime.now(), 4, 5, 2, 4),
            Candle(datetime.now(), 4, 5, 1, 4),
            Candle(datetime.now(), 4, 5, 3, 4),
        ]
    )

    swings = detect_two_bar_swings(bars)

    assert len(swings) == 1
    assert not swings[0].is_high