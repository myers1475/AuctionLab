from auctionlab.research.experiments.observation import Observation
from auctionlab.research.experiments.observation_log import ObservationLog


def test_observation_log():

    log = ObservationLog()

    log.add(
        Observation(
            current_price=100,
            target_name="PDH",
            target_price=110,
        )
    )

    assert len(log) == 1
    assert log.observations[0].target_name == "PDH"