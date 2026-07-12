from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Observation:
    current_price: float

    target_name: str
    target_price: float