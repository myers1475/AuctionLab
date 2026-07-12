from auctionlab.research.active_hypothesis import ActiveHypothesis
from auctionlab.research.hypothesis_builder import build_hypothesis


def test_active_hypothesis():

    hypothesis = build_hypothesis(
        observation="Bullish iFVG",
        inference="Nearest UPO = PDH",
        prediction="Reach PDH",
    )

    active = ActiveHypothesis(
        hypothesis=hypothesis,
    )

    assert active.bars_elapsed == 0
    assert active.mae == 0.0
    assert active.mfe == 0.0