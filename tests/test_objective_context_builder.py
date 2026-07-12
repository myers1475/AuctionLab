from dataclasses import dataclass

from auctionlab.inference.objective_context_builder import (
    build_objective_context,
)
from auctionlab.inference.upo_repository import UPORepository


@dataclass(frozen=True)
class FakeUPO:
    rep_price: float


def test_context():

    repo = UPORepository(
        swings=(FakeUPO(90), FakeUPO(110)),
        previous_days=(),
        previous_weeks=(),
        sessions=(),
    )

    context = build_objective_context(
        100,
        repo,
    )

    assert context.upside_objective.rep_price == 110
    assert context.downside_objective.rep_price == 90