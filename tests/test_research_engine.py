from auctionlab.research.hypothesis_builder import build_hypothesis
from auctionlab.research.research_engine import ResearchEngine


def test_research_engine():

    engine = ResearchEngine()

    hypothesis = build_hypothesis(
        observation="Bullish iFVG",
        inference="Nearest UPO = PDH",
        prediction="Reach PDH",
    )

    engine.process(
        snapshot=None,
        hypothesis=hypothesis,
    )

    assert len(engine.tracker) == 1