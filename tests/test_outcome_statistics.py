from auctionlab.research.experiments.outcome import Outcome
from auctionlab.research.experiments.outcome_log import OutcomeLog
from auctionlab.research.experiments.outcome_statistics import calculate


def test_outcome_statistics():

    log = OutcomeLog()

    log.add(
        Outcome(
            observation_time=None,
            outcome_time=None,
            target_kind="PDH",
            target_price=100,
            reached=True,
            bars_to_outcome=5,
        )
    )

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

    stats = calculate(log)

    assert stats.total == 2
    assert stats.reached == 1
    assert stats.unreached == 1
    assert stats.hit_rate == 0.5