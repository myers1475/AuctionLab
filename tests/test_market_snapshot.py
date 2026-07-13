from datetime import datetime

from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective
from auctionlab.observation.market_snapshot import MarketSnapshot


def test_market_snapshot():

    snapshot = MarketSnapshot(
        timestamp=datetime.now(),
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