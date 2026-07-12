from auctionlab.research.completed_research import CompletedResearch
from auctionlab.research.hypothesis import Hypothesis
from auctionlab.research.hypothesis_outcome import HypothesisOutcome
from auctionlab.research.research_result import ResearchResult


def complete_research(
    hypothesis: Hypothesis,
    outcome: HypothesisOutcome,
    bars_to_resolution: int,
    mae: float,
    mfe: float,
) -> CompletedResearch:

    result = ResearchResult(
        outcome=outcome,
        bars_to_resolution=bars_to_resolution,
        mae=mae,
        mfe=mfe,
    )

    return CompletedResearch(
        hypothesis=hypothesis,
        result=result,
    )