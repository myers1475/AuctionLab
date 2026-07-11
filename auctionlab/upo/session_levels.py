from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SessionLevels:
    session: str
    high: float
    low: float