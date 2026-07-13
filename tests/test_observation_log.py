from auctionlab.inference.control import Control
from auctionlab.research.experiments.observation import Observation
from auctionlab.research.experiments.observation_log import ObservationLog


def test_observation_log():

    log = ObservationLog()

    log.add(
        Observation(
            timestamp=None,
            current_price=100,
            visible_objectives=(),
            nearest_objective=None,
            control=Control.NEUTRAL,
        )
    )

    assert len(log) == 1
    assert log.observations[0].current_price == 100