from datetime import datetime

from auctionlab.observation.swing_detector import detect_swings
from auctionlab.reality.bar_series import BarSeries
from auctionlab.reality.candle import Candle


def test_detects_one_swing_high():
    ts = datetime.now()

    bars = BarSeries(
        [
            Candle(ts, 1, 2, 1, 2),
            Candle(ts, 2, 5, 2, 4),
            Candle(ts, 3, 3, 2, 2),
        ]
    )

    swings = detect_swings(bars)

    assert len(swings) == 1
    assert swings[0].timestamp == ts
    assert swings[0].is_high


def test_detects_one_swing_low():
    ts = datetime.now()

    bars = BarSeries(
        [
            Candle(ts, 4, 5, 2, 4),
            Candle(ts, 4, 5, 1, 4),
            Candle(ts, 4, 5, 3, 4),
        ]
    )

    swings = detect_swings(bars)

    assert len(swings) == 1
    assert swings[0].timestamp == ts
    assert not swings[0].is_high