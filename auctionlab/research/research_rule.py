from __future__ import annotations

from typing import Protocol

from auctionlab.observation.market_snapshot import MarketSnapshot
from auctionlab.research.hypothesis import Hypothesis


class ResearchRule(Protocol):

    def evaluate(
        self,
        snapshot: MarketSnapshot,
    ) -> list[Hypothesis]:
        ...