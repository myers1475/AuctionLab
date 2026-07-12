from auctionlab.reality.bar_series import BarSeries
from auctionlab.research.displacement import is_displacement
from auctionlab.research.fvg_filters import minimum_gap_size
from auctionlab.upo.fvg import FairValueGap
from auctionlab.upo.fvg_detector import detect_bullish_fvgs


def detect_quality_bullish_fvgs(
    bars: BarSeries,
    minimum_gap: float = 0.0,
    minimum_body_ratio: float = 0.65,
) -> list[FairValueGap]:
    fvgs = detect_bullish_fvgs(bars)

    fvgs = minimum_gap_size(
        fvgs,
        minimum_gap,
    )

    quality: list[FairValueGap] = []

    for fvg in fvgs:
        index = next(
            i
            for i, bar in enumerate(bars)
            if bar.timestamp == fvg.created
        )

        displacement = bars[index - 1]

        if is_displacement(
            displacement,
            minimum_body_ratio,
        ):
            quality.append(fvg)

    return quality