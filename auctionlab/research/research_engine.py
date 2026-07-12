from auctionlab.observation.market_snapshot import MarketSnapshot
from auctionlab.research.hypothesis import Hypothesis
from auctionlab.research.hypothesis_tracker import HypothesisTracker


class ResearchEngine:

    def __init__(self):
        self._tracker = HypothesisTracker()

    @property
    def tracker(self) -> HypothesisTracker:
        return self._tracker

    def process(
        self,
        snapshot: MarketSnapshot,
        hypothesis: Hypothesis | None,
    ) -> None:

        if hypothesis is not None:
            self._tracker.add(hypothesis)