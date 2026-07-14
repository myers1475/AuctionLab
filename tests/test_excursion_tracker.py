from datetime import datetime

from auctionlab.reality.candle import Candle

from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective

from auctionlab.research.experiments.excursion_tracker import (
    ExcursionTracker,
)
from auctionlab.research.experiments.observation import Observation


def test_excursion_tracker():

    tracker = ExcursionTracker(
        Observation(
            timestamp=None,
            current_price=100,
            visible_objectives=(),
            nearest_objective=Objective(
                kind="PDH",
                price=110,
                source=None,
            ),
            control=Control.NEUTRAL,
        )
    )

    tracker.update(
        Candle(
            timestamp=datetime.now(),
            open=100,
            high=103,
            low=100,
            close=103,
            volume=None,
        )
    )

    tracker.update(
        Candle(
            timestamp=datetime.now(),
            open=103,
            high=103,
            low=98,
            close=98,
            volume=None,
        )
    )

    tracker.update(
        Candle(
            timestamp=datetime.now(),
            open=98,
            high=106,
            low=98,
            close=106,
            volume=None,
        )
    )

    assert tracker.maximum_favorable_excursion == 6
    assert tracker.maximum_adverse_excursion == -2