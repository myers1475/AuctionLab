from auctionlab.research.experiments.observation import Observation
from auctionlab.research.experiments.outcome import Outcome


def resolve(
    observation: Observation,
    snapshots,
):

    nearest = observation.nearest_objective

    if nearest is None:
        return None

    target = nearest.price
    is_high = target >= observation.current_price

    for bars, snapshot in enumerate(snapshots, start=1):

        if snapshot.timestamp <= observation.timestamp:
            continue

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
                maximum_favorable_excursion=None,
                maximum_adverse_excursion=None,
            )

    return Outcome(
        observation_time=observation.timestamp,
        outcome_time=None,
        target_kind=nearest.kind,
        target_price=target,
        reached=False,
        bars_to_outcome=None,
        maximum_favorable_excursion=None,
        maximum_adverse_excursion=None,
    )