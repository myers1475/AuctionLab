from auctionlab.research.experiments.observation import Observation
from auctionlab.research.experiments.observation_log import ObservationLog


def test_observation_log():

    log = ObservationLog()

    log.add(
        Observation(
            timestamp=None,
            current_price=100,
            objective_kind="PDH",
            objective_price=110,
            source=None,
        )
    )

    assert len(log) == 1
    assert log.observations[0].objective_kind == "PDH"