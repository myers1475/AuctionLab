from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from auctionlab.research.hypothesis_outcome import HypothesisOutcome


@dataclass(frozen=True)
class Hypothesis:
    created: datetime

    observation: str
    inference: str
    prediction: str

    outcome: HypothesisOutcome = HypothesisOutcome.PENDING
    completed: datetime | None = None