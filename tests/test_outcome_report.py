from auctionlab.research.experiments.outcome_report import print_report
from auctionlab.research.experiments.outcome_statistics import (
    OutcomeStatistics,
)


def test_print_report():

    statistics = OutcomeStatistics(
        total=10,
        reached=7,
        unreached=3,
        hit_rate=0.7,
        minimum_bars_to_target=1,
        median_bars_to_target=4,
        average_bars_to_target=4.5,
        maximum_bars_to_target=9,
        average_efficiency=1.25,
        average_reward_risk=2.10,
        average_progress=92.5,
    )

    print_report(statistics)