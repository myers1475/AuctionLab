from dataclasses import dataclass

from auctionlab.inference.dominant_objective import dominant_objective
from auctionlab.inference.objective_context import ObjectiveContext


@dataclass(frozen=True)
class FakeUPO:
    rep_price: float


def test_choose_upside():

    context = ObjectiveContext(
        current_price=100,
        upside_objective=FakeUPO(103),
        downside_objective=FakeUPO(90),
    )

    assert dominant_objective(context).rep_price == 103


def test_choose_downside():

    context = ObjectiveContext(
        current_price=100,
        upside_objective=FakeUPO(115),
        downside_objective=FakeUPO(98),
    )

    assert dominant_objective(context).rep_price == 98


def test_only_upside():

    context = ObjectiveContext(
        current_price=100,
        upside_objective=FakeUPO(110),
        downside_objective=None,
    )

    assert dominant_objective(context).rep_price == 110


def test_only_downside():

    context = ObjectiveContext(
        current_price=100,
        upside_objective=None,
        downside_objective=FakeUPO(90),
    )

    assert dominant_objective(context).rep_price == 90