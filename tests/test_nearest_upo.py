from datetime import datetime

from auctionlab.inference.nearest_upo import nearest_upo
from auctionlab.upo.upo import UPO, UPOStatus


class DummyUPO(UPO):
    def __init__(self, level):
        super().__init__(
            created=datetime.now(),
            status=UPOStatus.ACTIVE,
        )
        self.level = level


def test_nearest_upo():
    upos = [
        DummyUPO(100),
        DummyUPO(120),
        DummyUPO(150),
    ]

    nearest = nearest_upo(
        118,
        upos,
        lambda u: u.level,
    )

    assert nearest.level == 120