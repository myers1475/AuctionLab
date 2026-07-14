from datetime import datetime

from auctionlab.reality.candle import Candle

from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.control import Control
from auctionlab.observation.market_snapshot import MarketSnapshot
from auctionlab.research.experiment_runner import ExperimentRunner


class DummyExperiment:

    def run(self, snapshot):
        return None


def test_runner_returns_empty_log():

    runner = ExperimentRunner()

    candle = Candle(
        timestamp=datetime.now(),
        open=100,
        high=101,
        low=99,
        close=100,
        volume=None,
    )

    snapshots = [
        MarketSnapshot(
            timestamp=candle.timestamp,
            candle=candle,
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