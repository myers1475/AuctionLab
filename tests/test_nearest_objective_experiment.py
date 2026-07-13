from auctionlab.research.experiments.nearest_objective import run


def test_no_objectives_returns_none():

    result = run(
        timestamp=None,
        current_price=100,
        objectives=[],
    )

    assert result is None