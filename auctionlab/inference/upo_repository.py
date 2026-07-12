from dataclasses import dataclass

from auctionlab.observation.swing import Swing
from auctionlab.upo.previous_day import PreviousDay
from auctionlab.upo.previous_week import PreviousWeek
from auctionlab.upo.session_levels import SessionLevels


@dataclass(frozen=True)
class UPORepository:
    swings: tuple[Swing, ...]
    previous_days: tuple[PreviousDay, ...]
    previous_weeks: tuple[PreviousWeek, ...]
    sessions: tuple[SessionLevels, ...]