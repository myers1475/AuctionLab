from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective
from auctionlab.research.experiments.observation import Observation


def test_distance_to_target():

    observation = Observation(
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

    object.__setattr__(
        observation.nearest_objective,
        "_distance",
        10,
    )

    assert observation.distance_to_target == 10


def test_distance_to_target_none():

    observation = Observation(
        timestamp=None,
        current_price=100,
        visible_objectives=(),
        nearest_objective=None,
        control=Control.NEUTRAL,
    )

    assert observation.distance_to_target is None