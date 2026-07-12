from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PreviousDay:
    high: float
    low: float