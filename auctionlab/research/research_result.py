from __future__ import annotations

from dataclasses import dataclass

from auctionlab.research.hypothesis_outcome import HypothesisOutcome


@dataclass(frozen=True)
class ResearchResult:
    outcome: HypothesisOutcome

    bars_to_resolution: int

    mae: float
    mfe: float