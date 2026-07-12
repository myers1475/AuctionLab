from datetime import datetime

from auctionlab.reality.candle import Candle
from auctionlab.research.active_hypothesis import ActiveHypothesis
from auctionlab.research.active_hypothesis_updater import advance
from auctionlab.research.direction import Direction
from auctionlab.research.hypothesis_builder import build_hypothesis


def test_advance():

    active = ActiveHypothesis(
        hypothesis=build_hypothesis(
            observation="Bullish iFVG",
            inference="Nearest UPO = PDH",
            prediction="Reach PDH",
        ),
        entry_price=100,
    )

    candle = Candle(
        timestamp=datetime.now(),
        open=100,
        high=108,
        low=97,
        close=105,
    )

    advance(
        active,
        candle,
        Direction.LONG,
    )

    assert active.bars_elapsed == 1
    assert active.mae == 3
    assert active.mfe == 8