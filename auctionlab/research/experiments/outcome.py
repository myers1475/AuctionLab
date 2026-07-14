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

    distance_to_target: float | None
    percent_to_target: float | None

    @property
    def efficiency(self) -> float | None:

        if (
            self.maximum_favorable_excursion is None
            or self.distance_to_target in (None, 0)
        ):
            return None

        return (
            self.maximum_favorable_excursion
            / self.distance_to_target
        )