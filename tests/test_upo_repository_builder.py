from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.upo_repository_builder import build_repository


def test_build_repository():

    active = ActiveUPOs(
        swings=(),
        previous_days=(),
        previous_weeks=(),
        fvgs=(),
        ifvgs=(),
    )

    repo = build_repository(active)

    assert repo.swings == ()
    assert repo.previous_days == ()
    assert repo.previous_weeks == ()
    assert repo.sessions == ()