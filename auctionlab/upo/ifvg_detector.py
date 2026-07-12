from auctionlab.upo.fvg import FairValueGap
from auctionlab.upo.ifvg import InversionFairValueGap
from auctionlab.upo.upo import UPOStatus


def detect_ifvgs(
    fvgs: list[FairValueGap],
) -> list[InversionFairValueGap]:

    ifvgs = []

    for fvg in fvgs:
        if fvg.status != UPOStatus.COMPLETED:
            continue

        ifvgs.append(
            InversionFairValueGap(
                created=fvg.completed,
                high=fvg.high,
                low=fvg.low,
                bullish=not fvg.bullish,
                status=UPOStatus.ACTIVE,
            )
        )

    return ifvgs