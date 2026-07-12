from auctionlab.research.active_hypothesis import ActiveHypothesis
from auctionlab.research.hypothesis_outcome import HypothesisOutcome
from auctionlab.research.simple_resolver import resolve_long


def resolve(
    active: ActiveHypothesis,
    high: float,
    low: float,
    target_price: float,
    invalidation_price: float,
) -> HypothesisOutcome:

    return resolve_long(
        target_price=target_price,
        invalidation_price=invalidation_price,
        high=high,
        low=low,
    )