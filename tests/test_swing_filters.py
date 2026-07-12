from datetime import datetime

from auctionlab.observation.swing import Swing
from auctionlab.research.swing_filters import minimum_move
from auctionlab.reality.candle import Candle


def make_swing(price, high):

    candle = Candle(
        timestamp=datetime.now(),
        open=price,
        high=price,
        low=price,
        close=price,
    )

    return Swing(
        timestamp=datetime.now(),
        name="Swing",
        candle=candle,
        index=0,
        is_high=high,
    )


def test_minimum_move():

    swings = [
        make_swing(100, True),
        make_swing(101, False),
        make_swing(110, True),
    ]

    filtered = minimum_move(swings, 5)

    assert len(filtered) == 2