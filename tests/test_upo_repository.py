from auctionlab.inference.upo_repository import UPORepository


def test_repository():

    repo = UPORepository(
        swings=(),
        previous_days=(),
        previous_weeks=(),
        sessions=(),
    )

    assert repo.swings == ()
    assert repo.previous_days == ()
    assert repo.previous_weeks == ()
    assert repo.sessions == ()