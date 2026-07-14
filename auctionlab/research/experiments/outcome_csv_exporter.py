import csv
from pathlib import Path

from auctionlab.research.experiments.outcome_log import OutcomeLog
from auctionlab.research.experiments.outcome_statistics import (
    calculate_by_target_kind,
)


def export_outcomes(
    log: OutcomeLog,
    filename: str,
):

    Path(filename).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        filename,
        "w",
        newline="",
    ) as f:

        writer = csv.writer(f)

        writer.writerow(
            [
                "observation_time",
                "outcome_time",
                "target_kind",
                "target_price",
                "reached",
                "bars_to_outcome",
                "distance_to_target",
                "percent_to_target",
                "mfe",
                "mae",
                "efficiency",
            ]
        )

        for outcome in log:

            writer.writerow(
                [
                    outcome.observation_time,
                    outcome.outcome_time,
                    outcome.target_kind,
                    outcome.target_price,
                    outcome.reached,
                    outcome.bars_to_outcome,
                    outcome.distance_to_target,
                    outcome.percent_to_target,
                    outcome.maximum_favorable_excursion,
                    outcome.maximum_adverse_excursion,
                    outcome.efficiency,
                ]
            )

    summary_filename = filename.replace(".csv", "_by_target.csv")

    with open(
        summary_filename,
        "w",
        newline="",
    ) as f:

        writer = csv.writer(f)

        writer.writerow(
            [
                "target_kind",
                "observations",
                "targets_reached",
                "hit_rate",
            ]
        )

        for row in calculate_by_target_kind(log):

            writer.writerow(
                [
                    row.target_kind,
                    row.total,
                    row.reached,
                    row.hit_rate,
                ]
            )