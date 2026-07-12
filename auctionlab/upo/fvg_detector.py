from auctionlab.reality.bar_series import BarSeries
from auctionlab.upo.fvg import FairValueGap
from auctionlab.upo.upo import UPOStatus


def detect_bullish_fvgs(bars: BarSeries) -> list[FairValueGap]:
    fvgs: list[FairValueGap] = []

    for i in range(2, len(bars)):
        left = bars[i - 2]
        right = bars[i]

        if left.high >= right.low:
            continue

        status = UPOStatus.ACTIVE
        completed = None

        for future in bars[i + 1:]:
            if future.low <= left.high:
                status = UPOStatus.COMPLETED
                completed = future.timestamp
                break

        fvgs.append(
            FairValueGap(
                created=right.timestamp,
                high=right.low,
                low=left.high,
                bullish=True,
                status=status,
                completed=completed,
            )
        )

    return fvgs