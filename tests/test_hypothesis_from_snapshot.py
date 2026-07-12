from dataclasses import dataclass

from auctionlab.inference.objective_context import ObjectiveContext
from auctionlab.research.hypothesis_from_snapshot import (
    hypothesis_from_context,
)


@dataclass(frozen=True)
class FakeUPO:
    rep_price: float


def test_build_hypothesis_from_context():

    context = ObjectiveContext(
        current_price=100,
        upside_objective=FakeUPO(110),
        downside_objective=None,
    )

    hypothesis = hypothesis_from_context(context)

    assert hypothesis is not None
    assert hypothesis.prediction == "Price will seek 110"