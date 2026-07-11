from datetime import datetime

from auctionlab.observation.swing import Swing
from auctionlab.reality.candle import Candle
from auctionlab.upo.swing_status import swing_status
from auctionlab.upo.upo import UPOStatus


def candle(high: float, low: float):
    return Candle(
        timestamp=datetime.now(),
        open=1,
        high=high,
        low=low,
        close=1,
    )


def test_active_swing_high():
    swing = Swing(
        timestamp=datetime.now(),
        name="Swing High",
        candle=candle(100, 90),
        index=5,
        is_high=True,
    )

    assert swing_status(swing, 99, 80) == UPOStatus.ACTIVE


def test_completed_swing_high():
    swing = Swing(
        timestamp=datetime.now(),
        name="Swing High",
        candle=candle(100, 90),
        index=5,
        is_high=True,
    )

    assert swing_status(swing, 101, 80) == UPOStatus.COMPLETED


def test_active_swing_low():
    swing = Swing(
        timestamp=datetime.now(),
        name="Swing Low",
        candle=candle(100, 90),
        index=5,
        is_high=False,
    )

    assert swing_status(swing, 110, 91) == UPOStatus.ACTIVE


def test_completed_swing_low():
    swing = Swing(
        timestamp=datetime.now(),
        name="Swing Low",
        candle=candle(100, 90),
        index=5,
        is_high=False,
    )

    assert swing_status(swing, 110, 89) == UPOStatus.COMPLETED