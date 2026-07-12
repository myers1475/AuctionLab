from datetime import datetime

from auctionlab.research.fvg_filters import minimum_gap_size
from auctionlab.upo.fvg import FairValueGap
from auctionlab.upo.upo import UPOStatus


def test_minimum_gap_filter():
    fvgs = [
        FairValueGap(
            created=datetime.now(),
            high=105,
            low=100,
            bullish=True,
            status=UPOStatus.ACTIVE,
        ),
        FairValueGap(
            created=datetime.now(),
            high=101,
            low=100,
            bullish=True,
            status=UPOStatus.ACTIVE,
        ),
    ]

    filtered = minimum_gap_size(fvgs, 3)

    assert len(filtered) == 1
    assert filtered[0].high == 105