from __future__ import annotations

from dataclasses import dataclass

from auctionlab.observation.swing import Swing
from auctionlab.upo.session_levels import SessionLevels


@dataclass(frozen=True)
class MarketSnapshot:
    swings: tuple[Swing, ...]
    session_levels: tuple[SessionLevels, ...]