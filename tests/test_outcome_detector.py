from auctionlab.inference.control import Control
from auctionlab.inference.nearest_objective import Objective

from auctionlab.research.experiments.observation import Observation
from auctionlab.research.experiments.outcome_detector import detect_outcome


def test_detect_outcome():

    observation = Observation(
        timestamp=None,
        current_price=100,
        visible_objectives=(),
        nearest_objective=Objective(
            kind="PDH",
            price=110,
            source=None,
        ),
        control=Control.NEUTRAL,
    )

    outcome = detect_outcome(observation)

    assert outcome is not None
    assert outcome.target_kind == "PDH"
    assert outcome.target_price == 110
    assert outcome.reached is False