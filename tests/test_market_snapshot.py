from datetime import datetime

from auctionlab.observation.market_snapshot import MarketSnapshot
from auctionlab.upo.upo import UPO, UPOStatus


def test_market_snapshot():
    upo = UPO(
        created=datetime.now(),
        status=UPOStatus.ACTIVE,
    )

    snapshot = MarketSnapshot(
        active_upos=(upo,),
    )

    assert len(snapshot.active_upos) == 1
    assert snapshot.active_upos[0].status == UPOStatus.ACTIVE