from enum import Enum


class HypothesisOutcome(str, Enum):
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"