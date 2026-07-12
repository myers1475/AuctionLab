from dataclasses import dataclass

from auctionlab.inference.nearest_active_upo import nearest_active_upo
from auctionlab.inference.upo_repository import UPORepository


@dataclass(frozen=True)
class FakeUPO:
    rep_price: float


def test_nearest_active_upo():

    repo = UPORepository(
        swings=(FakeUPO(100),),
        previous_days=(FakeUPO(120),),
        previous_weeks=(FakeUPO(90),),
        sessions=(FakeUPO(108),),
    )

    nearest = nearest_active_upo(
        107,
        repo,
    )

    assert nearest.rep_price == 108