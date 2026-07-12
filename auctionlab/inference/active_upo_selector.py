from auctionlab.inference.upo_repository import UPORepository


def active_upos(repository: UPORepository) -> list:

    upos = []

    upos.extend(repository.swings)
    upos.extend(repository.previous_days)
    upos.extend(repository.previous_weeks)
    upos.extend(repository.sessions)

    return upos