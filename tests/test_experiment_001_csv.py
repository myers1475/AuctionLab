from pathlib import Path

from auctionlab.research.experiments.csv_exporter import export_csv
from auctionlab.research.experiments.observation import Observation
from auctionlab.research.experiments.observation_log import ObservationLog
from auctionlab.inference.control import Control


def test_export_csv(tmp_path):

    log = ObservationLog()

    log.add(
        Observation(
            timestamp=None,
            current_price=100,
            visible_objectives=(),
            nearest_objective=None,
            control=Control.NEUTRAL,
        )
    )

    filename = tmp_path / "test.csv"

    export_csv(
        log,
        str(filename),
    )

    assert filename.exists()