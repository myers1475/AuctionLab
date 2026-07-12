from dataclasses import dataclass

from auctionlab.inference.nearest_directional_upo import (
    nearest_downside_upo,
    nearest_upside_upo,
)
from auctionlab.inference.upo_repository import UPORepository


@dataclass(frozen=True)
class FakeUPO:
    rep_price: float


def test_nearest_upside():

    repo = UPORepository(
        swings=(FakeUPO(110), FakeUPO(130)),
        previous_days=(FakeUPO(120),),
        previous_weeks=(),
        sessions=(),
    )

    nearest = nearest_upside_upo(107, repo)

    assert nearest.rep_price == 110


def test_nearest_downside():

    repo = UPORepository(
        swings=(FakeUPO(90), FakeUPO(70)),
        previous_days=(FakeUPO(80),),
        previous_weeks=(),
        sessions=(),
    )

    nearest = nearest_downside_upo(87, repo)

    assert nearest.rep_price == 80