from __future__ import annotations

from math import inf

from auctionlab.upo.upo import UPO


def nearest_upo(
    price: float,
    upos: list[UPO],
    level_getter,
) -> UPO | None:
    nearest = None
    distance = inf

    for upo in upos:
        level = level_getter(upo)
        d = abs(level - price)

        if d < distance:
            distance = d
            nearest = upo

    return nearest