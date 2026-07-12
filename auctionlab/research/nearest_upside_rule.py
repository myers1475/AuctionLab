from auctionlab.observation.market_snapshot import MarketSnapshot

from auctionlab.research.hypothesis import Hypothesis
from auctionlab.research.hypothesis_builder import build_hypothesis


class NearestUpsideRule:

    def evaluate(
        self,
        snapshot: MarketSnapshot,
    ) -> list[Hypothesis]:

        objective = snapshot.nearest_objective

        if objective is None:
            return []

        if objective.price <= snapshot.current_price:
            return []

        return [
            build_hypothesis(
                observation="Market Snapshot",
                inference=f"Nearest upside objective = {objective.kind}",
                prediction=f"Price reaches {objective.price}",
            )
        ]