from auctionlab.research.experiments.excursion_tracker import (
    ExcursionTracker,
)
from auctionlab.research.experiments.observation import Observation
from auctionlab.research.experiments.outcome import Outcome


def resolve(
    observation: Observation,
    snapshots,
):

    nearest = observation.nearest_objective

    if nearest is None:
        return None

    tracker = ExcursionTracker(observation)

    target = nearest.price
    is_high = target >= observation.current_price

    distance_to_target = abs(target - observation.current_price)

    if distance_to_target == 0:
        percent_to_target = 100.0
    else:
        percent_to_target = 0.0

    for bars, snapshot in enumerate(snapshots, start=1):

        if snapshot.timestamp <= observation.timestamp:
            continue

        tracker.update(snapshot.current_price)

        if is_high:
            reached = snapshot.current_price >= target
        else:
            reached = snapshot.current_price <= target

        if reached:

            return Outcome(
                observation_time=observation.timestamp,
                outcome_time=snapshot.timestamp,
                target_kind=nearest.kind,
                target_price=target,
                reached=True,
                bars_to_outcome=bars,
                maximum_favorable_excursion=tracker.maximum_favorable_excursion,
                maximum_adverse_excursion=tracker.maximum_adverse_excursion,
                distance_to_target=distance_to_target,
                percent_to_target=percent_to_target,
            )

    return Outcome(
        observation_time=observation.timestamp,
        outcome_time=None,
        target_kind=nearest.kind,
        target_price=target,
        reached=False,
        bars_to_outcome=None,
        maximum_favorable_excursion=tracker.maximum_favorable_excursion,
        maximum_adverse_excursion=tracker.maximum_adverse_excursion,
        distance_to_target=distance_to_target,
        percent_to_target=percent_to_target,
    )