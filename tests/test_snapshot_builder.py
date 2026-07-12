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

    snapshot = build_snapshot(
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

    assert snapshot.control == Control.BULLISH
    assert snapshot.nearest_objective is not None
    assert snapshot.nearest_objective.kind == "PDH"