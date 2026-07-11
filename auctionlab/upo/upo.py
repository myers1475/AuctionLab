from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class UPOStatus(Enum):
    ACTIVE = "Active"
    COMPLETED = "Completed"


@dataclass(frozen=True)
class UPO:
    created: datetime
    status: UPOStatus = field(default=UPOStatus.ACTIVE, kw_only=True)