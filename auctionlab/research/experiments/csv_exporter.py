from __future__ import annotations

import csv
from pathlib import Path

from auctionlab.research.experiments.observation_log import ObservationLog


def export_csv(
    log: ObservationLog,
    filename: str,
) -> None:

    Path(filename).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        filename,
        "w",
        newline="",
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "timestamp",
                "price",
                "nearest_objective",
                "nearest_price",
                "control",
            ]
        )

        for observation in log.observations:

            nearest = observation.nearest_objective

            writer.writerow(
                [
                    observation.timestamp,
                    observation.current_price,
                    None if nearest is None else nearest.kind,
                    None if nearest is None else nearest.price,
                    observation.control.value,
                ]
            )