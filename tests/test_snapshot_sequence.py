from datetime import datetime

from auctionlab.reality.candle import Candle

from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective
from auctionlab.observation.market_snapshot import MarketSnapshot
from auctionlab.replay.snapshot_sequence import SnapshotSequence


def make_snapshot(price):

    candle = Candle(
        timestamp=datetime.now(),
        open=price,
        high=price,
        low=price,
        close=price,
        volume=None,
    )

    return MarketSnapshot(
        timestamp=candle.timestamp,
        candle=candle,
        current_price=price,
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
            price=price,
            source=None,
        ),
    )


def test_snapshot_sequence():

    sequence = SnapshotSequence()

    sequence.add(make_snapshot(100))
    sequence.add(make_snapshot(101))

    assert len(sequence) == 2
    assert sequence.latest().nearest_objective.price == 101