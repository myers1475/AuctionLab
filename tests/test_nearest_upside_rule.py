from dataclasses import dataclass

from auctionlab.research.nearest_upside_rule import NearestUpsideRule


@dataclass(frozen=True)
class FakeObjective:
    kind: str
    price: float


@dataclass(frozen=True)
class FakeSnapshot:
    current_price: float
    nearest_objective: FakeObjective | None


def test_rule_creates_hypothesis():

    snapshot = FakeSnapshot(
        current_price=100,
        nearest_objective=FakeObjective(
            kind="PDH",
            price=110,
        ),
    )

    hypothesis = NearestUpsideRule().evaluate(snapshot)

    assert hypothesis is not None
    assert hypothesis.prediction == "Price reaches 110"


def test_rule_returns_none():

    snapshot = FakeSnapshot(
        current_price=100,
        nearest_objective=None,
    )

    assert NearestUpsideRule().evaluate(snapshot) is None