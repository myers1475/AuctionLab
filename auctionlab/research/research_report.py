from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResearchReport:
    active: int
    completed: int

    @property
    def total(self) -> int:
        return self.active + self.completed