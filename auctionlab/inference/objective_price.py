from auctionlab.upo.fvg import FairValueGap
from auctionlab.upo.ifvg import InversionFairValueGap


def fvg_price(fvg: FairValueGap) -> float:
    return (fvg.high + fvg.low) / 2


def ifvg_price(ifvg: InversionFairValueGap) -> float:
    return (ifvg.high + ifvg.low) / 2