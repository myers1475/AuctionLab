from __future__ import annotations

from dataclasses import dataclass

from auctionlab.upo.upo import UPO


@dataclass(frozen=True)
class MarketSnapshot:
    active_upos: tuple[UPO, ...]