from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Observation:
    timestamp: datetime

    current_price: float

    objective_kind: str
    objective_price: float

    source: object