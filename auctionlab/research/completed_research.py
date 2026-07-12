from __future__ import annotations

from dataclasses import dataclass

from auctionlab.research.hypothesis import Hypothesis
from auctionlab.research.research_result import ResearchResult


@dataclass(frozen=True)
class CompletedResearch:
    hypothesis: Hypothesis
    result: ResearchResult