from auctionlab.research.experiments.outcome import Outcome
from auctionlab.research.experiments.outcome_log import OutcomeLog


def make_outcome(reached: bool) -> Outcome:

    return Outcome(
        observation_time=None,
        outcome_time=None,
        target_kind="PDH",
        target_price=100,
        reached=reached,
        bars_to_outcome=None,
        maximum_favorable_excursion=None,
        maximum_adverse_excursion=None,
        distance_to_target=None,
        percent_to_target=None,
    )


def test_outcome_log():

    log = OutcomeLog()

    log.add(make_outcome(False))

    assert len(log) == 1


def test_reached_filter():

    log = OutcomeLog()

    log.add(make_outcome(True))
    log.add(make_outcome(False))
    log.add(make_outcome(True))

    assert len(log.reached()) == 2


def test_unreached_filter():

    log = OutcomeLog()

    log.add(make_outcome(True))
    log.add(make_outcome(False))
    log.add(make_outcome(False))

    assert len(log.unreached()) == 2