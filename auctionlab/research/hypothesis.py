from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

from auctionlab.research.hypothesis_outcome import HypothesisOutcome


@dataclass(frozen=True)
class Hypothesis:
    id: UUID

    created: datetime

    observation: str
    inference: str
    prediction: str

    outcome: HypothesisOutcome = HypothesisOutcome.PENDING
    completed: datetime | None = None

    @staticmethod
    def create(
        observation: str,
        inference: str,
        prediction: str,
    ) -> "Hypothesis":

        return Hypothesis(
            id=uuid4(),
            created=datetime.now(),
            observation=observation,
            inference=inference,
            prediction=prediction,
        )