from __future__ import annotations

from dataclasses import dataclass

from auctionlab.research.experiments.outcome_log import OutcomeLog


@dataclass(frozen=True)
class OutcomeStatistics:
    total: int
    reached: int
    unreached: int
    hit_rate: float


def calculate(
    log: OutcomeLog,
) -> OutcomeStatistics:

    total = len(log)
    reached = sum(
        outcome.reached
        for outcome in log.outcomes
    )
    unreached = total - reached

    hit_rate = (
        reached / total
        if total
        else 0.0
    )

    return OutcomeStatistics(
        total=total,
        reached=reached,
        unreached=unreached,
        hit_rate=hit_rate,
    )