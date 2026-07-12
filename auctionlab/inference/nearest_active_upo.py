from auctionlab.inference.active_upo_selector import active_upos
from auctionlab.inference.upo_repository import UPORepository


def nearest_active_upo(
    current_price: float,
    repository: UPORepository,
):

    upos = active_upos(repository)

    if not upos:
        return None

    return min(
        upos,
        key=lambda upo: abs(upo.rep_price - current_price),
    )