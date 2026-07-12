from datetime import datetime

from auctionlab.inference.objective_price import (
    fvg_price,
    ifvg_price,
)
from auctionlab.upo.fvg import FairValueGap
from auctionlab.upo.ifvg import InversionFairValueGap
from auctionlab.upo.upo import UPOStatus


def test_fvg_midpoint():
    fvg = FairValueGap(
        created=datetime.now(),
        high=110,
        low=100,
        bullish=True,
        status=UPOStatus.ACTIVE,
    )

    assert fvg_price(fvg) == 105


def test_ifvg_midpoint():
    ifvg = InversionFairValueGap(
        created=datetime.now(),
        high=120,
        low=100,
        bullish=False,
        status=UPOStatus.ACTIVE,
    )

    assert ifvg_price(ifvg) == 110