from auctionlab.research.active_hypothesis import ActiveHypothesis
from auctionlab.research.hypothesis_builder import build_hypothesis
from auctionlab.research.hypothesis_outcome import HypothesisOutcome
from auctionlab.research.research_evaluator import complete_research
from auctionlab.research.research_session import ResearchSession


def test_research_session():

    session = ResearchSession()

    hypothesis = ActiveHypothesis(
        hypothesis=build_hypothesis(
            observation="Bullish iFVG",
            inference="Nearest UPO = PDH",
            prediction="Reach PDH",
        ),
        entry_price=100,
    )

    session.add(hypothesis)

    assert len(session.active) == 1

    completed = complete_research(
        hypothesis.hypothesis,
        HypothesisOutcome.SUCCESS,
        bars_to_resolution=8,
        mae=3,
        mfe=17,
    )

    session.complete(completed)

    assert len(session.completed) == 1