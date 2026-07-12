from auctionlab.research.hypothesis_outcome import HypothesisOutcome


def resolve_long(
    target_price: float,
    invalidation_price: float,
    high: float,
    low: float,
) -> HypothesisOutcome:

    if high >= target_price:
        return HypothesisOutcome.SUCCESS

    if low <= invalidation_price:
        return HypothesisOutcome.FAILED

    return HypothesisOutcome.PENDING