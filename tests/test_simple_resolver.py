from auctionlab.research.hypothesis_outcome import HypothesisOutcome
from auctionlab.research.simple_resolver import resolve_long


def test_target_hit():

    outcome = resolve_long(
        target_price=110,
        invalidation_price=95,
        high=111,
        low=100,
    )

    assert outcome == HypothesisOutcome.SUCCESS


def test_invalidation_hit():

    outcome = resolve_long(
        target_price=110,
        invalidation_price=95,
        high=104,
        low=94,
    )

    assert outcome == HypothesisOutcome.FAILED


def test_still_pending():

    outcome = resolve_long(
        target_price=110,
        invalidation_price=95,
        high=108,
        low=98,
    )

    assert outcome == HypothesisOutcome.PENDING