from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Hypothesis:
    created: datetime

    observation: str
    inference: str
    prediction: str

    outcome: str | None = None
    completed: datetime | None = None