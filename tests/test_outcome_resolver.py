from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective
from auctionlab.observation.market_snapshot import MarketSnapshot
from auctionlab.research.experiments.observation import Observation
from auctionlab.research.experiments.outcome_resolver import resolve


def test_resolve_no_future_hit():

    observation = Observation(
        timestamp=1,
        current_price=100,
        visible_objectives=(),
        nearest_objective=Objective(
            kind="PDH",
            price=110,
            source=None,
        ),
        control=Control.NEUTRAL,
    )

    snapshots = [
        MarketSnapshot(
            timestamp=2,
            current_price=105,
            active_upos=None,
            control=Control.NEUTRAL,
            nearest_objective=None,
        )
    ]

    outcome = resolve(
        observation,
        snapshots,
    )

    assert outcome.reached is False