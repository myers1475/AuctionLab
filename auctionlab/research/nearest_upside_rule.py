from auctionlab.observation.market_snapshot import MarketSnapshot

from auctionlab.research.hypothesis_builder import build_hypothesis
from auctionlab.research.hypothesis import Hypothesis


class NearestUpsideRule:

    def evaluate(
        self,
        snapshot: MarketSnapshot,
    ) -> Hypothesis | None:

        objective = snapshot.nearest_objective

        if objective is None:
            return None

        if objective.price <= snapshot.current_price:
            return None

        return build_hypothesis(
            observation="Market Snapshot",
            inference=f"Nearest upside objective = {objective.kind}",
            prediction=f"Price reaches {objective.price}",
        )