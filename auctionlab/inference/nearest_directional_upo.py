from auctionlab.inference.active_upo_selector import active_upos
from auctionlab.inference.upo_repository import UPORepository


def nearest_upside_upo(
    current_price: float,
    repository: UPORepository,
):
    candidates = [
        upo
        for upo in active_upos(repository)
        if upo.rep_price > current_price
    ]

    if not candidates:
        return None

    return min(candidates, key=lambda upo: upo.rep_price)


def nearest_downside_upo(
    current_price: float,
    repository: UPORepository,
):
    candidates = [
        upo
        for upo in active_upos(repository)
        if upo.rep_price < current_price
    ]

    if not candidates:
        return None

    return max(candidates, key=lambda upo: upo.rep_price)