import csv
from pathlib import Path

from auctionlab.research.experiments.outcome_log import OutcomeLog


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
            ]
        )

        for outcome in log.outcomes:

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
                ]
            )