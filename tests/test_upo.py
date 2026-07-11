from datetime import datetime

from auctionlab.upo.upo import UPO, UPOStatus


def test_upo():
    upo = UPO(
        created=datetime.now(),
        status=UPOStatus.ACTIVE,
    )

    assert upo.status == UPOStatus.ACTIVE