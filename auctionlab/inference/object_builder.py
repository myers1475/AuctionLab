from __future__ import annotations

from auctionlab.inference.nearest_objective import Objective
from auctionlab.inference.active_upos import ActiveUPOs


def build_objectives(
    active_upos: ActiveUPOs,
) -> list[Objective]:

    objectives: list[Objective] = []

    for swing in active_upos.swings:

        objectives.append(
            Objective(
                kind=swing.name,
                price=swing.candle.high if swing.is_high else swing.candle.low,
                source=swing,
            )
        )

    for previous_day in active_upos.previous_days:

        objectives.append(
            Objective(
                kind="Previous Day High",
                price=previous_day.high,
                source=previous_day,
            )
        )

        objectives.append(
            Objective(
                kind="Previous Day Low",
                price=previous_day.low,
                source=previous_day,
            )
        )

    for previous_week in active_upos.previous_weeks:

        objectives.append(
            Objective(
                kind="Previous Week High",
                price=previous_week.high,
                source=previous_week,
            )
        )

        objectives.append(
            Objective(
                kind="Previous Week Low",
                price=previous_week.low,
                source=previous_week,
            )
        )

    return objectives