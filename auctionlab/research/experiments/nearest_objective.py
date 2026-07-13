from auctionlab.observation.market_snapshot import MarketSnapshot

from auctionlab.research.experiments.observation import Observation


def run(
    snapshot: MarketSnapshot,
):

    if snapshot.nearest_objective is None:
        return None

    return Observation(
        timestamp=snapshot.timestamp,
        current_price=snapshot.current_price,
        objective_kind=snapshot.nearest_objective.kind,
        objective_price=snapshot.nearest_objective.price,
        source=snapshot.nearest_objective.source,
    )