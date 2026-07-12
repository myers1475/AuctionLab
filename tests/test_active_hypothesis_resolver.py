from auctionlab.research.active_hypothesis import ActiveHypothesis
from auctionlab.research.active_hypothesis_resolver import resolve
from auctionlab.research.hypothesis_builder import build_hypothesis
from auctionlab.research.hypothesis_outcome import HypothesisOutcome


def test_resolve_success():

    active = ActiveHypothesis(
        hypothesis=build_hypothesis(
            observation="Bullish iFVG",
            inference="Nearest UPO = PDH",
            prediction="Reach PDH",
        ),
        entry_price=100,
    )

    outcome = resolve(
        active,
        high=111,
        low=99,
        target_price=110,
        invalidation_price=95,
    )

    assert outcome == HypothesisOutcome.SUCCESS


def test_resolve_failed():

    active = ActiveHypothesis(
        hypothesis=build_hypothesis(
            observation="Bullish iFVG",
            inference="Nearest UPO = PDH",
            prediction="Reach PDH",
        ),
        entry_price=100,
    )

    outcome = resolve(
        active,
        high=103,
        low=94,
        target_price=110,
        invalidation_price=95,
    )

    assert outcome == HypothesisOutcome.FAILED