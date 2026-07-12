from auctionlab.upo.fvg import FairValueGap


def minimum_gap_size(
    fvgs: list[FairValueGap],
    minimum: float,
) -> list[FairValueGap]:
    return [
        fvg
        for fvg in fvgs
        if (fvg.high - fvg.low) >= minimum
    ]