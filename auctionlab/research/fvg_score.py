from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FVGScore:
    htf: bool
    atr: bool
    displacement: bool
    near_upo: bool
    control: bool
    inversion: bool

    @property
    def total(self) -> int:
        return sum(
            (
                self.htf,
                self.atr,
                self.displacement,
                self.near_upo,
                self.control,
                self.inversion,
            )
        )