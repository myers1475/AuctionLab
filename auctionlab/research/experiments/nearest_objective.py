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
        visible_objectives=(snapshot.nearest_objective,),
        nearest_objective=snapshot.nearest_objective,
        control=snapshot.control,
    )