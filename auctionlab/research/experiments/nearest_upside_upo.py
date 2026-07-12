from auctionlab.inference.nearest_directional_upo import nearest_upside_upo
from auctionlab.inference.upo_repository import UPORepository

from auctionlab.research.experiments.observation import Observation


def run(
    current_price: float,
    repository: UPORepository,
):

    target = nearest_upside_upo(
        current_price=current_price,
        repository=repository,
    )

    if target is None:
        return None

    return Observation(
        current_price=current_price,
        target_name=target.name,
        target_price=target.rep_price,
    )