from auctionlab.research.hypothesis_outcome import HypothesisOutcome
from auctionlab.research.research_result import ResearchResult


def test_research_result():

    result = ResearchResult(
        outcome=HypothesisOutcome.SUCCESS,
        bars_to_resolution=12,
        mae=4.25,
        mfe=38.50,
    )

    assert result.outcome == HypothesisOutcome.SUCCESS
    assert result.bars_to_resolution == 12
    assert result.mae == 4.25
    assert result.mfe == 38.50