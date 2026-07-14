from datetime import datetime

from auctionlab.reality.candle import Candle

from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective
from auctionlab.observation.market_snapshot import MarketSnapshot


def test_market_snapshot():

    candle = Candle(
        timestamp=datetime.now(),
        open=101,
        high=102,
        low=100,
        close=101,
        volume=None,
    )

    snapshot = MarketSnapshot(
        timestamp=candle.timestamp,
        candle=candle,
        current_price=101,
        active_upos=ActiveUPOs(
            swings=(),
            previous_days=(),
            previous_weeks=(),
            fvgs=(),
            ifvgs=(),
        ),
        control=Control.BULLISH,
        nearest_objective=Objective(
            kind="PDH",
            price=100,
            source=None,
        ),
    )

    assert snapshot.current_price == 101