from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Outcome:
    observation_time: datetime
    outcome_time: datetime | None

    target_kind: str
    target_price: float

    reached: bool
    bars_to_outcome: int | None

    maximum_favorable_excursion: float | None
    maximum_adverse_excursion: float | None