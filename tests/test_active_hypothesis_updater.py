from auctionlab.research.active_hypothesis import ActiveHypothesis
from auctionlab.research.active_hypothesis_updater import advance
from auctionlab.research.hypothesis_builder import build_hypothesis


def test_advance():

    active = ActiveHypothesis(
        hypothesis=build_hypothesis(
            observation="Bullish iFVG",
            inference="Nearest UPO = PDH",
            prediction="Reach PDH",
        )
    )

    advance(
        active,
        mae=3.5,
        mfe=8.0,
    )

    assert active.bars_elapsed == 1
    assert active.mae == 3.5
    assert active.mfe == 8.0