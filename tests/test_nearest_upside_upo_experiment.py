from auctionlab.inference.upo_repository import UPORepository
from auctionlab.research.experiments.nearest_upside_upo import run


def test_experiment_runs():

    repository = UPORepository(
        swings=(),
        previous_days=(),
        previous_weeks=(),
        sessions=(),
    )

    result = run(
        current_price=100,
        repository=repository,
    )

    assert result is None