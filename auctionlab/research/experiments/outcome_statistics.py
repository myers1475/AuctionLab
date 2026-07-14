from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, median

from auctionlab.research.experiments.outcome_log import OutcomeLog


@dataclass(frozen=True)
class OutcomeStatistics:
    total: int
    reached: int
    unreached: int
    hit_rate: float

    minimum_bars_to_target: int | None
    median_bars_to_target: float | None
    average_bars_to_target: float | None
    maximum_bars_to_target: int | None


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

    bars = [
        outcome.bars_to_outcome
        for outcome in log.outcomes
        if outcome.bars_to_outcome is not None
    ]

    if bars:
        minimum_bars = min(bars)
        median_bars = median(bars)
        average_bars = mean(bars)
        maximum_bars = max(bars)
    else:
        minimum_bars = None
        median_bars = None
        average_bars = None
        maximum_bars = None

    return OutcomeStatistics(
        total=total,
        reached=reached,
        unreached=unreached,
        hit_rate=hit_rate,
        minimum_bars_to_target=minimum_bars,
        median_bars_to_target=median_bars,
        average_bars_to_target=average_bars,
        maximum_bars_to_target=maximum_bars,
    )