from auctionlab.research.active_hypothesis import ActiveHypothesis
from auctionlab.research.active_hypothesis_manager import (
    ActiveHypothesisManager,
)
from auctionlab.research.completed_research import CompletedResearch


class ResearchSession:

    def __init__(self):

        self.active = ActiveHypothesisManager()

        self.completed: list[CompletedResearch] = []

    def add(
        self,
        hypothesis: ActiveHypothesis,
    ) -> None:

        self.active.add(hypothesis)

    def complete(
        self,
        research: CompletedResearch,
    ) -> None:

        self.completed.append(research)