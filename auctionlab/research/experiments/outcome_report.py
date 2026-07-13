from auctionlab.research.experiments.outcome_statistics import (
    OutcomeStatistics,
)


def print_report(
    statistics: OutcomeStatistics,
) -> None:

    print()
    print("Experiment 001 Results")
    print("----------------------------")
    print(f"Total Observations : {statistics.total}")
    print(f"Targets Reached    : {statistics.reached}")
    print(f"Targets Missed     : {statistics.unreached}")
    print(f"Hit Rate           : {statistics.hit_rate:.2%}")