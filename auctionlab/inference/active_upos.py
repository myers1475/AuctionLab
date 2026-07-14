from __future__ import annotations

from dataclasses import dataclass

from auctionlab.observation.swing import Swing
from auctionlab.upo.fvg import FairValueGap
from auctionlab.upo.ifvg import InversionFairValueGap
from auctionlab.upo.previous_day import PreviousDay
from auctionlab.upo.previous_week import PreviousWeek


@dataclass(frozen=True)
class ActiveUPOs:
    swings: tuple[Swing, ...]
    previous_days: tuple[PreviousDay, ...]
    previous_weeks: tuple[PreviousWeek, ...]
    fvgs: tuple[FairValueGap, ...]
    ifvgs: tuple[InversionFairValueGap, ...]

    def all(self):

        return (
            self.swings
            + self.previous_days
            + self.previous_weeks
            + self.fvgs
            + self.ifvgs
        )