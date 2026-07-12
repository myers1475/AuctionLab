from auctionlab.inference.active_upos import ActiveUPOs
from auctionlab.inference.upo_repository import UPORepository


def build_repository(
    active_upos: ActiveUPOs,
) -> UPORepository:

    return UPORepository(
        swings=active_upos.swings,
        previous_days=active_upos.previous_days,
        previous_weeks=active_upos.previous_weeks,
        sessions=(),
    )