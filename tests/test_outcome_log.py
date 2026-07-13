from auctionlab.research.experiments.outcome import Outcome
from auctionlab.research.experiments.outcome_log import OutcomeLog


def test_outcome_log():

    log = OutcomeLog()

    log.add(
        Outcome(
            observation_time=None,
            outcome_time=None,
            target_kind="PDH",
            target_price=100,
            reached=False,
            bars_to_outcome=None,
        )
    )

    assert len(log) == 1