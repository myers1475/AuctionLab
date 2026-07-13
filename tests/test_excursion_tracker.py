from auctionlab.inference.control import Control

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
            nearest_objective=None,
            control=Control.NEUTRAL,
        )
    )

    tracker.update(103)
    tracker.update(98)
    tracker.update(106)

    assert tracker.maximum_favorable_excursion == 6
    assert tracker.maximum_adverse_excursion == -2