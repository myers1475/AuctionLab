from datetime import datetime

from auctionlab.observation.market_structure_builder import build_market_structure
from auctionlab.observation.swing import Swing
from auctionlab.reality.candle import Candle


def candle():
    return Candle(
        timestamp=datetime.now(),
        open=1,
        high=2,
        low=0,
        close=1,
    )


def test_market_structure():
    ts = datetime.now()

    swings = [
        Swing(ts, "Swing High", candle(), 5, True),
        Swing(ts, "Swing Low", candle(), 8, False),
        Swing(ts, "Swing High", candle(), 10, True),
    ]

    structure = build_market_structure(swings)

    assert structure.swing_high.index == 10
    assert structure.swing_low.index == 8