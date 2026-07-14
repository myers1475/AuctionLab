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

    print()
    print("Time to Target")
    print("----------------------------")
    print(f"Minimum Bars      : {statistics.minimum_bars_to_target}")
    print(f"Median Bars       : {statistics.median_bars_to_target}")
    print(f"Average Bars      : {statistics.average_bars_to_target:.2f}")
    print(f"Maximum Bars      : {statistics.maximum_bars_to_target}")