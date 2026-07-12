from auctionlab.research.active_hypothesis import ActiveHypothesis
from auctionlab.research.active_hypothesis_manager import (
    ActiveHypothesisManager,
)
from auctionlab.research.hypothesis_builder import build_hypothesis


def test_manager():

    manager = ActiveHypothesisManager()

    manager.add(
        ActiveHypothesis(
            hypothesis=build_hypothesis(
                observation="Bullish iFVG",
                inference="Nearest UPO = PDH",
                prediction="Reach PDH",
            ),
            entry_price=100.0,
        )
    )

    assert len(manager) == 1
    assert len(manager.active) == 1