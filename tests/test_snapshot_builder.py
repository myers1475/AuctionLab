from datetime import datetime

from auctionlab.reality.candle import Candle

from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective
from auctionlab.inference.snapshot_builder import build_snapshot


def test_snapshot_builder():

    objectives = [
        Objective(
            kind="PDH",
            price=100,
            source=None,
        )
    ]

    candle = Candle(
        timestamp=datetime.now(),
        open=101,
        high=102,
        low=100,
        close=101,
        volume=None,
    )

    snapshot = build_snapshot(
        timestamp=candle.timestamp,
        candle=candle,
        current_price=101,
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