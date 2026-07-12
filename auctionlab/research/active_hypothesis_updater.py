from auctionlab.research.active_hypothesis import ActiveHypothesis


def advance(
    active: ActiveHypothesis,
    mae: float,
    mfe: float,
) -> ActiveHypothesis:

    active.bars_elapsed += 1

    active.mae = max(active.mae, mae)
    active.mfe = max(active.mfe, mfe)

    return active