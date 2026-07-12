from auctionlab.research.completed_research import CompletedResearch
from auctionlab.research.hypothesis_builder import build_hypothesis
from auctionlab.research.hypothesis_outcome import HypothesisOutcome
from auctionlab.research.research_result import ResearchResult


def test_completed_research():

    hypothesis = build_hypothesis(
        observation="Bullish iFVG",
        inference="Nearest UPO = PDH",
        prediction="Reach PDH",
    )

    result = ResearchResult(
        outcome=HypothesisOutcome.SUCCESS,
        bars_to_resolution=12,
        mae=4.5,
        mfe=38.0,
    )

    completed = CompletedResearch(
        hypothesis=hypothesis,
        result=result,
    )

    assert completed.hypothesis == hypothesis
    assert completed.result == result