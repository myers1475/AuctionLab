from __future__ import annotations

from collections import defaultdict

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

    def by_target_kind(self) -> dict[str, list[Outcome]]:

        groups: dict[str, list[Outcome]] = defaultdict(list)

        for outcome in self._outcomes:
            groups[outcome.target_kind].append(outcome)

        return dict(groups)

    def __iter__(self):

        return iter(self._outcomes)

    def __len__(self):

        return len(self._outcomes)