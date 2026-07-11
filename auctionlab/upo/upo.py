from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class UPOStatus(Enum):
    ACTIVE = "Active"
    COMPLETED = "Completed"


@dataclass(frozen=True)
class UPO:
    created: datetime
    status: UPOStatus