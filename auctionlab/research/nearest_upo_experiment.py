from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NearestUPOExperiment:
    target_name: str
    target_price: float

    reached: bool = False