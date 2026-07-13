from datetime import datetime

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

    snapshot = build_snapshot(
        timestamp=datetime.now(),
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