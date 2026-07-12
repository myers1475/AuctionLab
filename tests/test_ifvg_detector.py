from datetime import datetime

from auctionlab.upo.fvg import FairValueGap
from auctionlab.upo.ifvg_detector import detect_ifvgs
from auctionlab.upo.upo import UPOStatus


def test_ifvg_created_from_completed_fvg():

    fvg = FairValueGap(
        created=datetime.now(),
        high=105,
        low=100,
        bullish=True,
        status=UPOStatus.COMPLETED,
        completed=datetime.now(),
    )

    ifvgs = detect_ifvgs([fvg])

    assert len(ifvgs) == 1
    assert ifvgs[0].bullish is False
    assert ifvgs[0].high == 105
    assert ifvgs[0].low == 100