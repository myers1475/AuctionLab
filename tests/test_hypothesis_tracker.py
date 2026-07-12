from auctionlab.research.hypothesis_builder import build_hypothesis
from auctionlab.research.hypothesis_tracker import (
    HypothesisTracker,
)


def test_tracker():

    tracker = HypothesisTracker()

    tracker.add(
        build_hypothesis(
            observation="Bullish iFVG",
            inference="Nearest UPO = PDH",
            prediction="Reach PDH",
        )
    )

    assert len(tracker) == 1
    assert len(tracker.hypotheses) == 1