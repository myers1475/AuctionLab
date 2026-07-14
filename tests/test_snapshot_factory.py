from datetime import datetime

from auctionlab.reality.candle import Candle

from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective
from auctionlab.replay.snapshot_factory import build_snapshot


def test_snapshot_factory():

    objectives = [
        Objective(
            kind="PDH",
            price=105,
            source=None,
        ),
        Objective(
            kind="Swing High",
            price=120,
            source=None,
        ),
    ]

    candle = Candle(
        timestamp=datetime.now(),
        open=103,
        high=104,
        low=102,
        close=103,
        volume=None,
    )

    snapshot = build_snapshot(
        timestamp=candle.timestamp,
        candle=candle,
        current_price=103,
        objectives=objectives,
        active_upos=ActiveUPOs(
            swings=(),
            previous_days=(),
            previous_weeks=(),
            fvgs=(),
            ifvgs=(),
        ),
        control=Control.BULLISH,
    )

    assert snapshot.nearest_objective.kind == "PDH"