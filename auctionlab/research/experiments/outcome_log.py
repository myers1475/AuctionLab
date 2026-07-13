from __future__ import annotations

from auctionlab.research.experiments.outcome import Outcome


class OutcomeLog:

    def __init__(self):
        self._outcomes: list[Outcome] = []

    @property
    def outcomes(self):
        return self._outcomes

    def add(
        self,
        outcome: Outcome,
    ) -> None:

        self._outcomes.append(outcome)

    def __len__(self):

        return len(self._outcomes)