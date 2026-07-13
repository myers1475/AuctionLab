from auctionlab.observation.market_snapshot import MarketSnapshot

from auctionlab.research.experiments.observation import Observation
from auctionlab.research.experiments.outcome import Outcome


def resolve(
    observation: Observation,
    snapshots,
):

    nearest = observation.nearest_objective

    if nearest is None:
        return None

    for bars, snapshot in enumerate(snapshots, start=1):

        if snapshot.timestamp <= observation.timestamp:
            continue

        if snapshot.current_price == nearest.price:

            return Outcome(
                observation_time=observation.timestamp,
                outcome_time=snapshot.timestamp,
                target_kind=nearest.kind,
                target_price=nearest.price,
                reached=True,
                bars_to_outcome=bars,
            )

    return Outcome(
        observation_time=observation.timestamp,
        outcome_time=None,
        target_kind=nearest.kind,
        target_price=nearest.price,
        reached=False,
        bars_to_outcome=None,
    )