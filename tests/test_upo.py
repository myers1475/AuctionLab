from datetime import datetime

from auctionlab.upo.upo import UPO, UPOStatus


def test_upo_defaults_to_active():
    upo = UPO(created=datetime.now())

    assert upo.status == UPOStatus.ACTIVE