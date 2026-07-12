from datetime import datetime

from auctionlab.upo.fvg import FairValueGap
from auctionlab.upo.upo import UPOStatus


def test_create_fvg():
    fvg = FairValueGap(
        created=datetime.now(),
        high=100,
        low=95,
        bullish=True,
        status=UPOStatus.ACTIVE,
    )

    assert fvg.high == 100
    assert fvg.low == 95
    assert fvg.bullish
    assert fvg.status == UPOStatus.ACTIVE