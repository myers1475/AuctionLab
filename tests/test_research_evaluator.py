from auctionlab.research.hypothesis_builder import build_hypothesis
from auctionlab.research.hypothesis_outcome import HypothesisOutcome
from auctionlab.research.research_evaluator import complete_research


def test_complete_research():

    hypothesis = build_hypothesis(
        observation="Bullish iFVG",
        inference="Nearest UPO = PDH",
        prediction="Reach PDH",
    )

    completed = complete_research(
        hypothesis=hypothesis,
        outcome=HypothesisOutcome.SUCCESS,
        bars_to_resolution=11,
        mae=3.25,
        mfe=27.50,
    )

    assert completed.result.outcome == HypothesisOutcome.SUCCESS
    assert completed.result.bars_to_resolution == 11