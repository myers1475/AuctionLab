from __future__ import annotations

from dataclasses import dataclass

from auctionlab.research.hypothesis import Hypothesis


@dataclass
class ActiveHypothesis:
    hypothesis: Hypothesis

    bars_elapsed: int = 0

    mae: float = 0.0
    mfe: float = 0.0