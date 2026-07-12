from auctionlab.inference.nearest_directional_upo import nearest_upside_upo
from auctionlab.inference.upo_repository import UPORepository


def run(
    current_price: float,
    repository: UPORepository,
):
    return nearest_upside_upo(
        current_price=current_price,
        repository=repository,
    )