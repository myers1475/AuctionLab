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
    )

    print_report(statistics)