from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PreviousWeek:
    high: float
    low: float