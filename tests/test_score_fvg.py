from datetime import datetime

from auctionlab.research.score_fvg import score_fvg
from auctionlab.upo.fvg import FairValueGap
from auctionlab.upo.upo import UPOStatus


def test_score_fvg():
    fvg = FairValueGap(
        created=datetime.now(),
        high=105,
        low=100,
        bullish=True,
        status=UPOStatus.ACTIVE,
    )

    score = score_fvg(
        fvg,
        htf=True,
        atr=False,
        displacement=True,
        near_upo=True,
        control=True,
        inversion=False,
    )

    assert score.total == 4