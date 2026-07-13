from datetime import datetime

from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.observation.market_snapshot import MarketSnapshot

from auctionlab.research.experiments.nearest_objective import run


def test_no_objectives_returns_none():

    snapshot = MarketSnapshot(
        timestamp=datetime.now(),
        current_price=100,
        active_upos=ActiveUPOs(
            swings=(),
            previous_days=(),
            previous_weeks=(),
            fvgs=(),
            ifvgs=(),
        ),
        control=Control.NEUTRAL,
        nearest_objective=None,
    )

    result = run(snapshot)

    assert result is None