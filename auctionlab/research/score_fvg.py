from auctionlab.research.fvg_score import FVGScore
from auctionlab.upo.fvg import FairValueGap


def score_fvg(
    fvg: FairValueGap,
    *,
    htf: bool,
    atr: bool,
    displacement: bool,
    near_upo: bool,
    control: bool,
    inversion: bool,
) -> FVGScore:
    return FVGScore(
        htf=htf,
        atr=atr,
        displacement=displacement,
        near_upo=near_upo,
        control=control,
        inversion=inversion,
    )