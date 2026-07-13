from datetime import datetime

from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.observation.market_snapshot import MarketSnapshot
from auctionlab.research.experiment_runner import ExperimentRunner


class DummyExperiment:

    def run(self, snapshot):
        return None


def test_runner_returns_empty_log():

    runner = ExperimentRunner()

    snapshots = [
        MarketSnapshot(
            timestamp=datetime.now(),
            current_price=100,
            active_upos=ActiveUPOs(
                swings=(),
                previous_days=(),
                previous_weeks=(),
                fvgs=(),
                ifvgs=(),
            ),
            control=Control.NEUTRAL,
            nearest_objective=None,
        )
    ]

    log = runner.run(
        snapshots=snapshots,
        experiment=DummyExperiment(),
    )

    assert len(log) == 0