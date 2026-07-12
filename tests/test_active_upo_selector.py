from auctionlab.inference.active_upo_selector import active_upos
from auctionlab.inference.upo_repository import UPORepository


def test_active_upos():

    repo = UPORepository(
        swings=(1, 2),
        previous_days=(3,),
        previous_weeks=(4,),
        sessions=(5, 6),
    )

    assert active_upos(repo) == [1, 2, 3, 4, 5, 6]