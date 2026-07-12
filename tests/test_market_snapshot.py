from datetime import datetime

from auctionlab.observation.market_snapshot import MarketSnapshot
from auctionlab.observation.swing import Swing
from auctionlab.reality.candle import Candle
from auctionlab.upo.session_levels import SessionLevels


def candle():
    return Candle(
        timestamp=datetime.now(),
        open=1,
        high=2,
        low=0,
        close=1,
    )


def test_market_snapshot():
    swing = Swing(
        timestamp=datetime.now(),
        name="Swing High",
        candle=candle(),
        index=5,
        is_high=True,
    )

    asia = SessionLevels(
        session="Asia",
        high=100,
        low=90,
    )

    snapshot = MarketSnapshot(
        swings=(swing,),
        session_levels=(asia,),
    )

    assert len(snapshot.swings) == 1
    assert len(snapshot.session_levels) == 1